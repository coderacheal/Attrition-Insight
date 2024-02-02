import streamlit as st
import pandas as pd
import pyodbc
from utils import feature_descriptions


#Set page configurations
st.set_page_config(
    page_title='View Data',
    layout='wide',
    page_icon='📄'
)


#set page title
st.title('Proprietory Data & Features')


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

#Call the connection and store as a variable
conn = init_connection()


#Create a function to query the database and cache the results
@st.cache_data()
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
        df = pd.DataFrame.from_records(rows, columns = [column[0] for column in cur.description])
        return df


#Initialise columns to be selected from database
if 'selected_columns' not in st.session_state:
    st.session_state['selected_columns'] = ["All Columns"]


def select_specific_features():

    if st.session_state['selected_columns'][0] == 'All Columns':
        selected_columns = '*'
    # elif len(st.session_state['selected_columns']) > 2 and st.session_state['selected_columns'] 

    #Run query to get all features initially
    query = run_query(f"SELECT {selected_columns} FROM LP2_Telco_churn_first_3000")

    #Create 2 columns for showing feature description and specific columns
    col1, col2 = st.columns(2)

    with col1:
        # Use st.expander to create an expandable section
        with st.expander(" ##### **Expand to learn about features**"):
            st.markdown(feature_descriptions)

    with col2:
        st.multiselect('Select Specific Columns to view', options=['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents','tenure', 'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn', 'All Columns'], key='selected_columns', on_change=run_query, kwargs=query)
    
    st.write('')
    st.write('## Results from Database 🗃️...')
    st.dataframe(query)


#Call function
select_specific_features()

st.write(st.session_state)
