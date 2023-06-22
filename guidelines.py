import streamlit as st

def guidelines():
    st.sidebar.subheader("Guidelines")
    st.sidebar.write(
        """1. Navigate to app page. Fill in the information"""
    )
    st.sidebar.write("""
        1.1. In the table, copy-paste the Analytical Statement, Evidence etc. If you have more data, click on Add Row to create another row.
        If there are multiple evidences, create a new row and paste the evidence in respective cell and you can leave the Analytical Statement cell empty in tha row.
        """
    )
    st.sidebar.write("1.2. If you want to delete the row, click on the checkbox and click on Delete Row.")
    st.sidebar.write("1.3. Fill in the Data Dump table in the same fashion. If any of the fields is empty, leave it empty.")
    st.sidebar.write("1.4. Click on the Submit button to store the data in the database. Confirmed by an acknowledged message.")
    st.sidebar.write("1.5. Click on the Submit button to store the data in the database. Confirmed by an acknowledged message.")
    st.sidebar.write("2. In the View Data page, view the already uploaded data in a tabular form.")
    st.sidebar.write("3. The data can be downloaded in excel/csv format you clicking on Generate Download link button.")
