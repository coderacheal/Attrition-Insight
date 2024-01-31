import streamlit as st
import joblib


# Set page configurations
st.set_page_config(
    page_title='Predict Attrition',
    layout='wide',
)

#Load model and encoder
model = joblib.load('models/finished_model.joblib')
encoder  = joblib.load('models/encoder.joblib')


st.title('Predict Attrition')

#Create a form to get all input features
with st.form('form key'):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write('### Personal Info')
        age = st.number_input('Enter your age', key='age')
        marital_status = st.selectbox('Select your marital status', options=['single', 'married'], key='marital_statuse')
        distance_from_home = st.number_input('What is you distance from home', key='distance_from_home')
        monthly_income = st.number_input('Enter your salary(In years)', key='monthly_income')

    with col2:
        st.write('### Work Info')
        department = st.selectbox('Select your department', options=['Human Resource', 'Agric'], key='department')
        education = st.number_input('Enter the number of education years', key='education')
        education_field = st.selectbox('Enter what field of Education you have', options=['Science', 'Management'], key='education_field')
        years_at_company = st.number_input('How many years have you worked in this company', key='years_at_company')

    with col3:
        st.write('### Satifaction Index')
        environment_satisfaction = st.slider('Rate your satisfaction with the environement', max_value=5, step=1, key='environment_satisfaction')
        job_satisfaction = st.slider('Rate your job satisfaction', max_value=5, step=1, key='job_satisfaction')
        work_life_balance = st.slider('Rate your work-life balance', max_value=5, step=1, key='work_life_balance')
        number_of_companies_worked = st.slider('How many companies have you worked for', max_value=20, step=1, key='number_of_companies_worked')

        
    #Add a submit button
    st.form_submit_button('### **Submit**', type='primary', use_container_width=True)


data_input = []
st.write(st.session_state)