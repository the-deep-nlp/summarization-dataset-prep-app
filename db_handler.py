import boto3
import streamlit as st
from botocore.exceptions import ClientError

def write_to_db(final_dict, region_name="us-east-1"):
    """ write data to the dynamodb """
    try:
        dynamodb = boto3.resource("dynamodb", region_name=region_name)
        table = dynamodb.Table("summarization_tbl")
        response = table.put_item(Item=final_dict)
        return response
    except ClientError as cerr:
        st.write(f"Database error occurred. ${cerr}")
    return None
