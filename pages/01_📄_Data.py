import streamlit as st
import pandas as pd
import pyodbc
from utils import feature_descriptions

st.set_page_config(
    page_title='Data',
    layout='wide',
    page_icon='📄'
)

st.title('Proprietory Data from IMB')

# Initialize connection and use st.cache_resource to only run once.
@st.cache_resource(show_spinner='Connecting to Database...')
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

# call the connection and store as a variable
conn = init_connection()


#Create a function to query the database and cache the results
@st.cache_data()
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()

        df = pd.DataFrame.from_records(rows, columns = [column[0] for column in cur.description])
        
        return df

data = run_query("SELECT * FROM LP2_Telco_churn_first_3000")
st.dataframe(data)


st.markdown('## Understanding The Features')
# Use st.expander to create an expandable section
with st.expander(" #### **Expand to learn about features**"):
    st.markdown(feature_descriptions)

