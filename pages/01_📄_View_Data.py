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

#set page title
st.title('Proprietory Data & Features 🗃️')
st.write('')


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


query = running_query(f"SELECT * FROM LP2_Telco_churn_first_3000")
st.dataframe(query)


@st.cache_data()
def select_cat_features():
    cat_columns = ['customerID', 'gender', 'MultipleLines', 'InternetService',
                        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                        'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod', 'Churn']
   
    cat_query = running_query(f"SELECT {', '.join(cat_columns)} FROM LP2_Telco_churn_first_3000")
    return cat_query


@st.cache_data()
def select_num_features():
    num_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']
   
    num_query = running_query(f"SELECT {', '.join(num_columns)} FROM LP2_Telco_churn_first_3000")
    return num_query


st.markdown('# More Information on Features and Select Columns')
# st.divider()
col1, col2 = st.columns(2)
with col1:
    with st.expander(" ##### **Expand to learn about features**"):
        st.markdown(feature_descriptions)
with col2:
    st.selectbox('Select Specific Features', options=['No column selected', 'View numeric columns', 'View categorical columns'], key='selected_columns')


if st.session_state['selected_columns'] == 'View categorical columns':
    st.write('### Showing results for Categorical Columns...')
    cat_results = select_cat_features()
    st.dataframe(cat_results)
elif st.session_state['selected_columns'] == 'View numeric columns':
    st.write('### Showing results for Numeric Columns...')
    num_results = select_num_features()
    st.dataframe(num_results)
else:
    pass
