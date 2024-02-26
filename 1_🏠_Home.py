import streamlit as st
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
    col1, col2 = st.columns(2)
    with col1:
        column_1
    with col2:
        st.write('### How to run application')
        st.code('''
        #activate virtual environment
        env/scripts/activate
        streamlit run 1_🏠_Home.py
        ''')
        column_2
        st.link_button('Repository on GitHub', url='https://github.com/coderacheal/Attrition-Meter', type='primary')

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.info('Enter username and password to use the app.')
    st.code("""
            Test Account
            Username: coderacheal
            Password: 123456""")
