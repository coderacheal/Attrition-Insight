import streamlit as st
import pandas as pd
from utils import feature_descriptions

# Set page configurations
st.set_page_config(
    page_title='View Data',
    layout='wide',
    page_icon='📄'
)

path = './data/attrition_data_ibm.csv'

@st.cache_data()
def select_all_features():
    df = pd.read_csv(path)
    data = df.drop('ColumnX', axis=1)
    return data


@st.cache_data()
def select_cat_features():
    df = pd.read_csv(path)
    data = df.select_dtypes(include='object')
    return data


@st.cache_data()
def select_num_features():
    df = pd.read_csv(path)
    data = df.select_dtypes(include='number')
    data = df.drop('ColumnX', axis=1)
    return data


# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.info('Login from the Home page to use app')
else:
    #Set page title
    st.markdown('### Proprietory Data from IBM 🛢️')

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

   