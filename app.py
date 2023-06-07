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
    "outliers": [" "]
})

with st.form("summ_tagging", clear_on_submit=True):
    project_options = ["ProjectE", "ProjectB", "ProjectC", "ProjectR"]
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

    # st.write(response)
    #st.dataframe(response["data"])
    # selected_rows = response["selected_rows"]
    # st.write(selected_rows)

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

    other_info = st.text_input("Other Info", help="Provide extra details if any")

    submit_btn = st.form_submit_button("Submit")

    if submit_btn:
        st.write("Submitted")
        st.dataframe(response["data"])
        st.write(response.keys())
        #st.experimental_rerun()


#st.write(response_dump)



# if len(selected_rows):
#     st.markdown('#### Selected')
#     dfs = pd.DataFrame(selected_rows)

#     dfsnet = dfs.drop(columns=['_selectedRowNodeInfo'])
#     st.dataframe(dfsnet)
#     # AgGrid(
#     #     dfsnet,
#     #     enable_enterprise_modules=False,
#     #     columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW,
#     #     reload_data=True,
#     #     key='product_selected'
#     # )