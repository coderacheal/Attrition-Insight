import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# hashed_pwd = stauth.hasher()

st.set_page_config(
    page_title='About',
    layout='centered',
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

authenticator.login()
# authenticator.register()


# with st.form('login-key'):
#     st.write('### **Log In**')
#     st.text_input('Enter your email')
#     st.text_input('Enter your password', type='password')
#     st.form_submit_button('Log In')

col1, col2 = st.columns(2)

with col1:
    st.write(f"""
    # App Name
    App Description
    ## Key Features
    - Data Visualization
    - Machine Learning Models Integration
    - Real-time Predictions
    ## User Benefits
    - Make data-driven decisions effortlessly.
    - Harness the power of machine learning without the complexity.
    ## Live Demo
    [Watch Demo Video](link) or [Get Started Now](link)
   
""")
    
with col2:
    st.write(
        """
    ## Machine Learning Integration
    - Supports popular models like Linear Regression, Random Forest, and Neural Networks.
    - Simple integration and user-friendly interface.
    ## Advanced Features
    - Customization options for model parameters.
    - Real-time predictions for up-to-the-minute insights.
    ## About
    Attrition Meter is developed by a passionate team of data scientists and engineers dedicated to simplifying data analysis and machine learning.
    ## Need Help?
    Contact us at  hello@rachealappiahkubi.com
    © 2024. All rights reserved.
    """
    )
    st.link_button('GitHub', url='https://github.com/coderacheal')
    st.link_button('Medium', url='https://medium.com/coderacheal')


st.write(st.session_state())