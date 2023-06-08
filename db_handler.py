import io
import base64
import boto3
from boto3.dynamodb.conditions import Attr
import pandas as pd
import streamlit as st
from botocore.exceptions import ClientError
from constants import VERSION

def write_to_db(
    final_dict,
    table_name="summarization_tbl",
    region_name="us-east-1"
):
    """ Write data to the dynamodb """
    try:
        dynamodb_client = boto3.resource("dynamodb", region_name=region_name)
        table = dynamodb_client.Table(table_name)
        response = table.put_item(Item=final_dict)
        return response
    except ClientError as cerr:
        st.write(f"Database error occurred. ${cerr}")
    return None

def download_data(
    table_name="summarization_tbl",
    region_name="us-east-1",
    output_file_name="summarization_data.xlsx"
):
    """
    Downloads the data from the dynamodb
    """
    try:
        dynamodb_client = boto3.resource("dynamodb", region_name=region_name)
        table = dynamodb_client.Table(table_name)

        response = table.scan(FilterExpression=Attr("version").eq(VERSION))
    except ClientError:
        response = None

    if response:
        items = response["Items"]
        towrite = io.BytesIO()
        output_df = pd.DataFrame(items)
        output_df.to_excel(towrite, index=False, header=True)
        towrite.seek(0)
        b64 = base64.b64encode(towrite.read()).decode()
        return f"""<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}"
            download={output_file_name}>Download output file (Excel)</a>"""
