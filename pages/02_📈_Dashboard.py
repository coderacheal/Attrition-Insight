import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Set page configurations
st.set_page_config(
    page_title='Dashboard',
    layout='wide',
    page_icon='📈'
)



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

# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.warning('### Login from the Home page to use app')
else:
    st.title('Attrition Dashboard')

    # Create a Plotly figure using Plotly Express
    fig = px.bar(data, x='Category', y='Values', title='Sample Bar Chart')

    # Display the Plotly figure in Streamlit
    st.plotly_chart(fig)

