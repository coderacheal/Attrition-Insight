import streamlit as st
import pandas as pd
import pyodbc
from utils import feature_descriptions

# Set page configurations
st.set_page_config(
    page_title='View Data',
    layout='wide',
    page_icon='📄'
)


# Initialize connection and use st.cache_resource to only run once.
@st.cache_resource(show_spinner='Connecting to Database 🗃️...')
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


# Call the connection and store as a variable
conn = init_connection()


# Create a function to query the database and cache the results
@st.cache_data()
def running_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
        df = pd.DataFrame.from_records(rows, columns=[column[0] for column in cur.description])
        return df


@st.cache_data()
def select_all_features():
    data = running_query("SELECT * FROM LP2_Telco_churn_first_3000")
    return data


@st.cache_data()
def select_cat_features():
    cat_columns = ['customerID', 'gender', 'MultipleLines', 'InternetService',
                        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                        'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod', 'Churn']
   
    data = running_query(f"SELECT {', '.join(cat_columns)} FROM LP2_Telco_churn_first_3000")
    return data


@st.cache_data()
def select_num_features():
    num_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']
   
    data = running_query(f"SELECT {', '.join(num_columns)} FROM LP2_Telco_churn_first_3000")
    return data


# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.warning('### Login from the Home page to use app')
else:
    #Set page title
    st.title('Proprietory Data from Vodafone 🛢️')

    with st.expander("Expand to learn about features"):
        st.markdown(feature_descriptions)

    # Additional Code for the Second Page
    col1, col2 = st.columns(2)
    with col1:
        pass
    with col2:
        st.selectbox('Select Specific Features', options=['All Columns','View numeric columns', 'View categorical columns', 'No column selected'], key='selected_columns')
    
    if st.session_state['selected_columns'] == 'All Columns':
        data = select_all_features()
        st.dataframe(data)
    elif st.session_state['selected_columns'] == 'View categorical columns':
        data = select_cat_features()
        st.dataframe(data)
    elif st.session_state['selected_columns'] == 'View numeric columns':
        data = select_num_features()
        st.dataframe(data)
    else:
        pass

    


