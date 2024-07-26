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


df = pd.read_csv('./data/attrition_data_ibm.csv')

def eda_visualizations():

    st.markdown('### Exploratory Data Analysis')
    col1, col2 = st.columns(2)

    with col1:
        age_histogram = px.histogram(df, x='Age', nbins=15, title='Age Distribution at IBM', color_discrete_sequence=['skyblue'])
        
        scatter_plot = px.scatter(df, x='Age', y='MonthlyIncome', color='Attrition',
                    title='Age vs Monthly Income (Colored by Attrition)',
                    color_discrete_map={'Yes': 'red', 'No': 'skyblue'}, height=650)

        #Show plots
        st.plotly_chart(age_histogram)
        st.plotly_chart(scatter_plot)
        
        
    with col2:
        # Melt the dataframe to long-form
        columns = ['Age', 'Department', 'DistanceFromHome', 'Education', 'EducationField',
        'EnvironmentSatisfaction', 'JobSatisfaction', 'MaritalStatus', 'NumCompaniesWorked', 'WorkLifeBalance','YearsAtCompany']

        df_long = pd.melt(df, value_vars=columns, var_name='Feature', value_name='Value')

        boxplot = px.box(df_long, x='Feature', y='Value',
                    title='Outliers in the dataset excluding Monthly Income')

        #Show plots
        correlation_heatmap = px.imshow(df.corr(numeric_only=True),
                                        color_continuous_scale='blues',
                                        labels=dict(color='Correlation'),
                                        title='Correlation Heatmap', width=800, height=650
                                        )

        
        st.plotly_chart(boxplot)
        st.plotly_chart(correlation_heatmap)
        

def dashboard_visualizations():

    st.markdown('### Attrition Dashboard & KPIs')
    col1, col2 = st.columns(2)

    with col1:

        st.write('')

        st.markdown(
            f"""
            <div style="background-color: #CCE5FF; border-radius: 10px; width: 80%; margin-top: 20px;" >
                <h3 style="margin-left: 30px">Quick Stats About Dataset</h3>
                <hr>
                <h5 style="margin-left: 30px"> Attrition Rate: {(df['Attrition'].value_counts(normalize=True).get('Yes', 0) * 100):.2f}%.</h5>
                <hr>
                <h5 style="margin-left: 30px">Average Monthly Income: ${df['MonthlyIncome'].mean():.2f}</h5>
                <hr>
                <h5 style="margin-left: 30px">Data Size: {df.size}</h5>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        # Create grouped bar chart
        barchart = px.bar(df, x='Department', color='Attrition', barmode='group',
                                color_discrete_map={'Yes': 'pink', 'No': 'skyblue'},
                                title='Attrition By Department')

        st.plotly_chart(barchart)
    
    col1, col2 = st.columns(2)

    with col1:
        # Calculate average monthly income by department
        average_income_df = df.groupby('Department')['MonthlyIncome'].mean().reset_index()

        colors = {'Sales': 'deepskyblue', 'Research & Development': 'pink', 'Human Resources': 'skyblue'}
        
        # Create horizontal bar chart
        average_income_chart = px.bar(average_income_df,
            x='Department',
            y='MonthlyIncome',
            title='Average Monthly Income by Department',
            color='Department',
            orientation='v',
            color_discrete_map=colors,
            text='MonthlyIncome'
            )
        
        # Format text on bars to display values with two decimal places
        average_income_chart.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        st.plotly_chart(average_income_chart)

    with col2:
        piechart = px.pie(df, names='Attrition', title='Attrition Percentage', color_discrete_sequence=[ 'skyblue', 'pink'])
        st.plotly_chart(piechart)


# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.info('Login from the Home page to use app')
else:

    col1, col2 = st.columns(2)

    with col2:
        st.selectbox('Select dashboard type', options=['EDA', 'KPIs'], key='dashboard_type')
    
    if st.session_state['dashboard_type'] == 'EDA':
        eda_visualizations()
    else:
        dashboard_visualizations()
