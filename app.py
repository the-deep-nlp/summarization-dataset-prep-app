import json
import uuid
import streamlit as st
import pandas as pd
from st_aggrid import (
    AgGrid,
    GridUpdateMode,
    ColumnsAutoSizeMode,
    AgGridTheme,
    DataReturnMode
)
from gridoptions import go, go_dump
from db_handler import write_to_db, download_data
from constants import VERSION
from guidelines import guidelines

if "RetrievalKeys" in st.session_state:
    del st.session_state["RetrievalKeys"]

def filter_lst(lst):
    """ Filters out whitespace or nan items """
    return list(filter(lambda x: x != " " and x != "nan", lst))

st.set_page_config(layout="wide")
data_df = pd.DataFrame({
    "analytical_statement":[" "],
    "comp_prev_months": [" "],
    "evidence": [" "]
})
data_dump_df = pd.DataFrame({
    "anecdotal":[" "],
    "too_old": [" "],
    "redundant":[" "],
    "outliers": [" "],
    "not_relevant": [" "]
})

data_download_btn = st.sidebar.button("Generate Download link")
if data_download_btn:
    st.sidebar.markdown(
        download_data(),
        unsafe_allow_html=True
    )

# Guidelines
guidelines()

with st.form("summ_tagging", clear_on_submit=True):
    project_options = [
        "Bangladesh",
        "Burkina Faso",
        "Columbia",
        "DRC",
        "Nigeria",
        "Syria",
        "Ukraine"
    ]
    project_options.sort() # sort in asc
    selected_project = st.selectbox("Projects", project_options)

    sectors_col, pillars_col, subpillars_col, other_tags = st.columns(4)

    sectors = sectors_col.text_input("Sectors", help="Enter sectors separated by comma")
    pillars = pillars_col.text_input("Pillars", help="Enter pillars separated by comma")
    subpillars = subpillars_col.text_input("Subpillars", help="Enter subpillars separated by comma")
    othertags = other_tags.text_input("Other Tags", help="Enter other tags separated by comma")

    published_date = st.date_input("Published on")

    response = AgGrid(
        data_df,
        gridOptions=go,
        update_mode=GridUpdateMode.VALUE_CHANGED,
        data_return_mode=DataReturnMode.AS_INPUT,
        allow_unsafe_jscode=True,
        height=400,
        width="100%",
        enable_enterprise_modules=True,
        theme=AgGridTheme.STREAMLIT,
        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW,
        wrapText=True,
        key='first',
        reload_data=True
    )

    st.subheader("Data Dump")

    response_dump = AgGrid(
        data_dump_df,
        gridOptions=go_dump,
        allow_unsafe_jscode=True,
        height=400,
        width="100%",
        enable_enterprise_modules=True,
        theme=AgGridTheme.STREAMLIT,
        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW,
        wrapText=True,
        key='second',
        reload_data=True
    )

    other_info = st.text_input("Other Information", help="Provide extra details if any")

    submit_btn = st.form_submit_button("Submit")

    if submit_btn:
        first_df = response["data"]
        first_df['analytical_statement'] = first_df['analytical_statement'].replace('nan', pd.NA).ffill()

        df_as_ev = first_df.groupby("analytical_statement")["evidence"].apply(list)
        df_as_cpm = first_df.groupby("analytical_statement")["comp_prev_months"].apply(list)
        
        as_ev_dict = json.loads(df_as_ev.to_json())
        as_cpm_dict = json.loads(df_as_cpm.to_json())

        for key, val in as_ev_dict.items():
            as_ev_dict[key] = filter_lst(val)
        
        for key, val in as_cpm_dict.items():
            as_cpm_dict[key] = filter_lst(val)

        summaries_lst = []
        for key, val in as_ev_dict.items():
            summaries_lst.append(
                {
                    "analytical_statement": key,
                    "evidence": val,
                    "comp_with_prev_month": as_cpm_dict[key] if key in as_cpm_dict else []
                }
            )

        # dump data
        second_df = response_dump["data"]
        anecdotal_lst = filter_lst(second_df["anecdotal"].tolist())
        too_old_lst = filter_lst(second_df["too_old"].tolist())
        redundant_lst = filter_lst(second_df["redundant"].tolist())
        outliers_lst = filter_lst(second_df["outliers"].tolist())
        not_relevant_lst = filter_lst(second_df["not_relevant"].tolist())

        main_dict = {
            "summ_key": str(uuid.uuid1()),
            "project_id": selected_project,
            "sectors": sectors,
            "pillars": pillars,
            "subpillars": subpillars,
            "other_tags": othertags,
            "published_on": str(published_date),
            "summaries": json.dumps(summaries_lst),
            "anecdotal": json.dumps(anecdotal_lst),
            "too_old": json.dumps(too_old_lst),
            "redundant": json.dumps(redundant_lst),
            "outliers": json.dumps(outliers_lst),
            "not_relevant": json.dumps(not_relevant_lst),
            "other_info": other_info,
            "version": VERSION
        }
        # Handle the database
        db_response = write_to_db(main_dict)
        if ("ResponseMetadata" in db_response and
                "HTTPStatusCode" in db_response["ResponseMetadata"]):
            if db_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                st.success("Successfully updated the database.")
            else:
                st.error("Failed to update the database.")
        else:
            st.error("Failed to update the database.")
