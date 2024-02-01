import streamlit as st
import pandas as pd
import pyodbc


st.title('More about the Data')

# Initialize connection.
# Use st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

conn = init_connection()


@st.cache_data()
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()

        df = pd.DataFrame.from_records(rows, columns = [column[0] for column in cur.description])
        df_now = st.dataframe(df)
        
        return df_now

data = run_query("SELECT * FROM LP2_Telco_churn_first_3000")
st.write(data)
