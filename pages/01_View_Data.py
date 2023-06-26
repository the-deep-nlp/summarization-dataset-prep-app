import streamlit as st
import pandas as pd
from guidelines import guidelines
from db_handler import get_db_data, download_data

st.set_page_config(layout="wide")

data_download_btn = st.sidebar.button("Generate Download link")
if data_download_btn:
    st.sidebar.markdown(
        download_data(),
        unsafe_allow_html=True
    )

# Guidelines
guidelines()

previous_p, next_p = st.columns([1, 1], gap="large")
previous_btn = previous_p.button("Previous")
next_btn = next_p.button("Next")

if "RetrievalKeys" not in st.session_state:
    st.session_state["RetrievalKeys"] = [None]
    data = get_db_data(prev_or_next=1)
    df = pd.DataFrame(data)
    st.dataframe(df)

if previous_btn:
    data = get_db_data(prev_or_next=0)
    if data:
        df = pd.DataFrame(data)
        if not df.empty:
            st.dataframe(df, use_container_width=True)

if next_btn:
    data = get_db_data(prev_or_next=1)
    if data:
        df = pd.DataFrame(data)
        if not df.empty:
            st.dataframe(df, use_container_width=True)

st.write("Note: Showing a maximum of 10 items per page.")