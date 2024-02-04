import streamlit as st
import joblib
import numpy as np
import pandas as pd


# Set page configurations
st.set_page_config(
    page_title='Prediction',
    layout='wide',
    page_icon='🤖'
)

#Choose model
def select_model():
    #Create 2 columns
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox('Select Model Type', options=['Random Forest Classifier', 'Decision Tree Classifier'], key='selected_model', placeholder="Select Model",)
    with col2:
        pass


# Initialise prediction in the session state
if "prediction" not in st.session_state:
    st.session_state['prediction'] = None

# Initialise prediction in the session state
if "pred_proba" not in st.session_state:
    st.session_state['pred_proba'] = None


#Initialise model
@st.cache_resource(show_spinner='Models Loading...')
def load_model():

    #Load model and encoder
    if st.session_state['selected_model'] == 'Random Forest Classifier':
        pipeline = joblib.load('models/finished_model.joblib')
    else:
        pipeline = joblib.load('models/finished_model.joblib')      

    encoder  = joblib.load('models/encoder.joblib')

    return pipeline, encoder


def predict_attrition(pipeline, encoder):
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

    # create the datafram with the values and column names
    df = pd.DataFrame(data, columns=columns)

    # Make a prediction and get probabilities
    pred_proba = pipeline.predict_proba(df)
    pred = pipeline.predict(df)
    pred = int(pred[0])

    classes_order = pipeline.classes_

    #Decode the prediction
    prediction = encoder.inverse_transform([pred])

    #Store the value in the session state
    st.session_state['prediction'] = prediction
    st.session_state['pred_proba'] = pred_proba
    st.session_state['classes_order'] = classes_order

    #Push df into a database

    return pred_proba, prediction


# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.warning('### Login from the Home page to use app')
else:
    if __name__ == '__main__':
        st.title('Predict Attrition')

        #Call model selection function
        select_model()

        #Create a form to get all input features
        with st.form('form key'):

            #Load model and encoder
            pipeline, encoder = load_model()

            #Divide form into 3 columns
            col1, col2, col3 = st.columns(3)

            with col1:
                st.write('### Personal Info 👩🏿')
                st.number_input('Enter your age', key='age', max_value=60, step=1)
                marital_status = st.selectbox('Select your marital status', options=['Single', 'Married', 'Divorced'], key='marital_status')
                st.number_input('What is you distance from home', key='distance_from_home', max_value=25)
                st.number_input('Enter your salary per month', key='monthly_income', min_value=1000, step=100)

            with col2:
                st.write('### Work Info 💼')
                st.selectbox('Select your department', options=['Sales', 'Research & Development', 'Human Resources'], key='department')
                st.number_input('Enter the number of education years', key='education', min_value=1, step=1)
                st.selectbox('Enter what field of Education you have', options=['Life Sciences', 'Other', 'Medical', 'Marketing','Technical Degree','Human Resources'], key='education_field')
                st.number_input('How many companies have you worked for', max_value=20, step=1, key='number_of_companies_worked')

            with col3:
                st.write('### Satifaction Index 😍')
                st.number_input('Rate your satisfaction with the environement', max_value=5, step=1, key='environment_satisfaction')
                st.number_input('Rate your job satisfaction', max_value=5, step=1, key='job_satisfaction')
                st.number_input('Rate your work-life balance', max_value=5, step=1, key='work_life_balance')
                st.number_input('How many years have you worked in this company', key='years_at_company', min_value=1, step=1)

                
            st.form_submit_button('## **Predict**', type='primary', use_container_width=False, on_click=predict_attrition, kwargs=dict(pipeline=pipeline, encoder=encoder))

    final_prediction = st.session_state["prediction"]
    pred_proba = st.session_state["pred_proba"]

    if not final_prediction:
        st.write("### Predictions show here ⬇️")
        st.divider()
    elif final_prediction == 'Yes':
        probability_of_yes = pred_proba[0][1] * 100
        st.markdown(f"### Employee will leave 🏃‍♂️ IBM with a {round(probability_of_yes, 2)}% probability.")
        st.divider()
    else:
        probability_of_no = pred_proba[0][0] * 100
        st.markdown(f"### Employee will stay 🧘‍♂️ at IBM with a {round(probability_of_no, 2)}% probability.")
        st.divider()


# st.write(st.session_state)