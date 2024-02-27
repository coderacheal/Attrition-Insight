import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title='History',
    page_icon='🕰️',
    layout='wide',
)


# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.info('Login from the Home page to use app')
else:
    st.markdown('## Prediction History ')

    # Check if history CSV file exists
    csv_path = './data/history.csv'

    csv_exists = os.path.exists(csv_path)


    if csv_exists:
        # Read and display the DataFrame
        history = pd.read_csv(csv_path)

        height = 300

        if history.shape[0] > 10:
            height = 500
        st.dataframe(history, height=height)
    else:
        # Display a friendly message
        st.info("No prediction history available yet. Make predictions to populate the history.")
