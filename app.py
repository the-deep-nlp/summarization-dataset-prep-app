import streamlit as st
import pandas as pd
from st_aggrid import (
    AgGrid,
    GridUpdateMode,
    ColumnsAutoSizeMode,
    AgGridTheme
)
from gridoptions import go, go_dump


project_options = ["ProjectE", "ProjectB", "ProjectC", "ProjectR"]
selected_project = st.selectbox("Projects", project_options)

sectors_col, pillars_col, subpillars_col, other_tags = st.columns(4)

sectors = sectors_col.text_input("Sectors", help="Enter sectors separated by comma")
pillars = pillars_col.text_input("Pillars", help="Enter pillars separated by comma")
subpillars = subpillars_col.text_input("Subpillars", help="Enter subpillars separated by comma")
othertags = other_tags.text_input("Other Tags", help="Enter other tags separated by comma")

published_date = st.date_input("Published on")

data_df = pd.DataFrame({"abc":["a"], "xyz": ["a"], "efg": ["a"]})

response = AgGrid(
    data_df,
    gridOptions=go,
    allow_unsafe_jscode=True,
    height=400,
    width="100%",
    theme=AgGridTheme.STREAMLIT,
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW,
    wrapText=True,
    key='first'
)

st.write(response)
st.dataframe(response["data"])
selected_rows = response["selected_rows"]
st.write(selected_rows)

data_dump_df = pd.DataFrame({"anecdotal":["a"], "too_old": ["a"], "redundant":["a"], "outliers": ["a"]})

response_dump = AgGrid(
    data_dump_df,
    gridOptions=go_dump,
    allow_unsafe_jscode=True,
    height=400,
    width="100%",
    theme=AgGridTheme.STREAMLIT,
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW,
    wrapText=True,
    key='second'
)

other_info = st.text_input("Other Info", help="Provide extra details if any")

st.write(response_dump)



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