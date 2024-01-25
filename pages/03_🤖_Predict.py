import streamlit as st
import joblib


#Load model and encoder

model = joblib.load('models/finished_model.joblib')
encoder  = joblib.load('models/encoder.joblib')

st.write(model)

# Age', 'Department', 'DistanceFromHome', 'Education', 'EducationField',
#        'EnvironmentSatisfaction', 'JobSatisfaction', 'MaritalStatus',
#        'MonthlyIncome', 'NumCompaniesWorked', 'WorkLifeBalance',
#        'YearsAtCompany'],

with st.form('form key'):
    age = st.number_input('Enter your age')
    department = st.selectbox('Select your department', options=['Human Resource', 'Agric'])
    distance_from_home = st.number_input('What is you distance from home')
    st.form_submit_button('submit')
