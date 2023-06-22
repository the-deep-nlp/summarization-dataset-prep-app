import io
import base64
import boto3
from boto3.dynamodb.conditions import Attr
import pandas as pd
import streamlit as st
from botocore.exceptions import ClientError
from constants import VERSION, AWS_REGION_NAME, DB_TABLE_NAME

# Dynamodb Initialization
dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION_NAME)
table = dynamodb.Table(DB_TABLE_NAME)

def write_to_db(
    final_dict
):
    """ Write data to the dynamodb """
    try:
        response = table.put_item(Item=final_dict)
        return response
    except ClientError as cerr:
        st.error(f"Database error occurred. ${cerr}")
    return None

def download_data(
    output_file_name="summarization_data.xlsx"
):
    """
    Downloads the data from the dynamodb
    """
    try:
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

def retrieve_db_data(prev_or_next, limit):
    """ Retrieve database data """
    if prev_or_next:
        handler_key = st.session_state["RetrievalKeys"][-1]
    else:
        try:
            st.session_state["RetrievalKeys"].pop()
            st.session_state["RetrievalKeys"].pop()
            handler_key = st.session_state["RetrievalKeys"][-1]
        except IndexError:
            st.session_state["RetrievalKeys"] = [None]
            handler_key = None

    if handler_key and handler_key != "End":
        response = table.scan(
            Limit=limit,
            ExclusiveStartKey=handler_key
        )
    elif handler_key == "End":
        st.warning("End of the Dataframe.")
        return None
    else:
        response = table.scan(
            Limit=limit
        )
    return response

def get_db_data(limit=1, prev_or_next=1):
    """
    Get data from the database
    """

    response = retrieve_db_data(prev_or_next, limit)
    if response:
        key = response["LastEvaluatedKey"] if "LastEvaluatedKey" in response else "End"
        if key == "End" and not response["Items"]:
            st.warning("End of the Dataframe.")
        st.session_state["RetrievalKeys"].append(key)
        return response["Items"]
    return None
