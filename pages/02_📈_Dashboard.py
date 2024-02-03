import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Set page configurations
st.set_page_config(
    page_title='Dashboard',
    layout='wide',
)

st.title('Attrition Dashboard')


def scatter_plot(dataframe):
    pass

def pie_chart_plot(dataframe):
    pass

def bar_chart():
    pass

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 15, 25]
})

# Create a Plotly figure using Plotly Express
fig = px.bar(data, x='Category', y='Values', title='Sample Bar Chart')

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)

