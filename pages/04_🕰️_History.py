import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title='History',
    page_icon='🕰️',
    layout='wide',
)

st.title('Prediction History ')

# Check if history CSV file exists
csv_path = './data/history.csv'
csv_exists = os.path.exists(csv_path)

if csv_exists:
    # Read and display the DataFrame
    history = pd.read_csv(csv_path)
    st.dataframe(history)
else:
    # Display a friendly message
    st.info("No prediction history available yet. Make predictions to populate the history.")
