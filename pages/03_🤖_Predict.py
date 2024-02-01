import streamlit as st
import joblib
import numpy as np
import pandas as pd


# Set page configurations
st.set_page_config(
    page_title='Predict Attrition',
    layout='wide',
)



#Initialise model
@st.cache_resource(show_spinner='Model Loading...')
def load_model():
    #Load model and encoder
    pipeline = joblib.load('models/finished_model.joblib')
    encoder  = joblib.load('models/encoder.joblib')

    return pipeline


def predict_attrition(pipeline):

    age = st.session_state['age']
    marital_status = st.session_state['marital_status']
    distance_from_home = st.session_state['distance_from_home']
    monthly_income = st.session_state['monthly_income']
    department = st.session_state['department']
    education = st.session_state['education']
    education_field = st.session_state['education_field']
    years_at_company = st.session_state['years_at_company']
    environment_satisfaction = st.session_state['environment_satisfaction']
    job_satisfaction = st.session_state['job_satisfaction']
    work_life_balance = st.session_state['work_life_balance']
    number_of_companies_worked = st.session_state['number_of_companies_worked']

    # Provide column names for the DataFrame
    columns = ['Age', 'Department', 'DistanceFromHome', 'Education', 'EducationField', 'EnvironmentSatisfaction', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'NumCompaniesWorked', 'WorkLifeBalance', 'YearsAtCompany']

    # Create a DataFrame with feature values
    data = [[age, department, distance_from_home, education, education_field, environment_satisfaction, job_satisfaction, marital_status, monthly_income, number_of_companies_worked, work_life_balance, years_at_company]]

    df = pd.DataFrame(data, columns=columns)

    pred = pipeline.predict(df)
    pred = pred[0]

    st.session_state['pred'] = pred



if __name__ == '__main__':
    st.title('Predict Attrition')

    #Create a form to get all input features
    with st.form('form key'):

        pipeline = load_model()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write('### Personal Info')
            age = st.number_input('Enter your age', key='age', max_value=60, step=1)
            marital_status = st.selectbox('Select your marital status', options=['Single', 'Married', 'Divorced'], key='marital_status')
            distance_from_home = st.number_input('What is you distance from home', key='distance_from_home', max_value=25)
            monthly_income = st.number_input('Enter your salary per year', key='monthly_income', min_value=10000, step=1000)

        with col2:
            st.write('### Work Info')
            department = st.selectbox('Select your department', options=['Sales', 'Research & Development', 'Human Resources'], key='department')
            education = st.number_input('Enter the number of education years', key='education', min_value=1, step=1)
            education_field = st.selectbox('Enter what field of Education you have', options=['Life Sciences', 'Other', 'Medical', 'Marketing','Technical Degree','Human Resources'], key='education_field')
            years_at_company = st.number_input('How many years have you worked in this company', key='years_at_company', min_value=1, step=1)

        with col3:
            st.write('### Satifaction Index')
            environment_satisfaction = st.slider('Rate your satisfaction with the environement', max_value=5, step=1, key='environment_satisfaction')
            job_satisfaction = st.slider('Rate your job satisfaction', max_value=5, step=1, key='job_satisfaction')
            work_life_balance = st.slider('Rate your work-life balance', max_value=5, step=1, key='work_life_balance')
            number_of_companies_worked = st.slider('How many companies have you worked for', max_value=20, step=1, key='number_of_companies_worked')

            
        #Add a submit button
        st.form_submit_button('### **Submit**', type='primary', use_container_width=True, on_click=predict_attrition, kwargs=dict(pipeline=pipeline))


if "pred" not in st.session_state:
    st.session_state['pred'] = None
# elif 

# if ''

st.write(st.session_state)