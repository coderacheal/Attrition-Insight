import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from utils import column_1, column_2


st.set_page_config(
    page_title='About',
    layout='wide',
    page_icon='🏠'
)


with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login(location='sidebar')

if st.session_state["authentication_status"]:
    authenticator.logout(location='sidebar', key='logout-button')
    st.write(f'Welcome *{st.session_state["name"]}*')
    col1, col2 = st.columns(2)
    with col1:
        column_1
    with col2:
        column_2
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('## Login to use Attrition Metre')

