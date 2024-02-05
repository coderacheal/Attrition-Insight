import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='History',
    page_icon='🕰️',
    layout='wide',
)

st.title('Prediction History ')

history = pd.read_csv('./data/history.csv')
st.dataframe(history)