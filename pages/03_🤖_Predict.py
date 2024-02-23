import streamlit as st
import joblib
import pandas as pd
import os
import datetime


# Set page configurations
st.set_page_config(
    page_title='Prediction',
    layout='wide',
    page_icon='🤖'
)


st.cache_resource(show_spinner='Model Loading')
def load_forest_pipeline():
    pipeline = joblib.load('./models/forest_pipeline.joblib')
    return pipeline


st.cache_resource(show_spinner='Model Loading')
def load_scv_pipeline():
    pipeline = joblib.load('./models/svc_pipeline.joblib')
    return pipeline


st.cache_resource()
def select_model():
    col1, col2 = st.columns(2)

    with col1:
        st.selectbox('Select a Model', options=['Random Forest', 'SVC'], key='selected_model')
    with col2:
        pass

    if st.session_state['selected_model'] == 'Random Forest':
        pipeline = load_forest_pipeline()
    else:
        pipeline = load_scv_pipeline()

    encoder = joblib.load('./models/encoder.joblib')

    return pipeline, encoder


def make_prediction(pipeline, encoder):
    age = st.session_state['age']
    department = st.session_state['department']
    distancefromhome = st.session_state['distancefromhome']
    education = st.session_state['education']
    education_field = st.session_state['education_field']
    environment_satisfaction = st.session_state['environment_satisfaction']
    job_satisfaction = st.session_state['job_satisfaction']
    marital_status = st.session_state['marital_status']
    monthly_income = st.session_state['monthly_income']
    number_of_companies_worked = st.session_state['number_of_companies_worked']
    work_life_balance = st.session_state['work_life_balance']
    years_at_company = st.session_state['years_at_company']

    columns = ['Age', 'Department', 'DistanceFromHome', 'Education', 'EducationField',
       'EnvironmentSatisfaction', 'JobSatisfaction', 'MaritalStatus',
        'MonthlyIncome', 'NumCompaniesWorked', 'WorkLifeBalance',
        'YearsAtCompany']
    
    data = [[age, department, distancefromhome, education, education_field, environment_satisfaction, job_satisfaction, marital_status, monthly_income,
             number_of_companies_worked, work_life_balance,  years_at_company]]
    
    #create a dataframe
    df = pd.DataFrame(data, columns=columns)

    #Make prediction
    pred = pipeline.predict(df)
    prediction  = int(pred[0])
    prediction = encoder.inverse_transform([prediction])

    #Get probabilities
    probability = pipeline.predict_proba(df)

    #Updating state
    st.session_state['prediction'] = prediction
    st.session_state['probability'] = probability

    #Add Attrition and time of prediction to dataframe
    df['Attrition'] = prediction
    df['Prediction_Time'] = datetime.date.today()

    #Push df into a history.csv and save DataFrame to a CSV file in append mode
    df.to_csv('./data/history.csv', mode='a', header=not os.path.exists('./data/history.csv'), index=False)

    return prediction, probability

if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None
if 'probability' not in st.session_state:
    st.session_state['probability'] = None


def display_form():
    pipeline, encoder = select_model()


    with st.form('input-feature'):

        #Divide form into 3 columns
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write('### Personal Info 👩🏿')
            st.number_input('Enter your age', key='age', min_value=18, max_value=60, step=1)
            st.selectbox('Select your marital status', options=['Single', 'Married', 'Divorced'], key='marital_status')
            st.number_input('What is you distance from home', key='distancefromhome', max_value=25, min_value=1)
            st.number_input('Enter your salary per month', key='monthly_income', min_value=1000, step=100)

        with col2:
            st.write('### Work Info 💼')
            st.selectbox('Select your department', options=['Sales', 'Research & Development', 'Human Resources'], key='department')
            st.number_input('Enter the number of education years', key='education', min_value=1, step=1)
            st.selectbox('Enter what field of Education you have', options=['Life Sciences', 'Other', 'Medical', 'Marketing','Technical Degree','Human Resources'], key='education_field')
            st.number_input('How many companies have you worked for', min_value=1, max_value=20, step=1, key='number_of_companies_worked')

        with col3:
            st.write('### Satifaction Index 😍')
            st.number_input('Rate your satisfaction with the environement', max_value=4, min_value=1, step=1, key='environment_satisfaction')
            st.number_input('Rate your job satisfaction', max_value=4, min_value=1, step=1, key='job_satisfaction')
            st.number_input('Rate your work-life balance', max_value=4, step=1, key='work_life_balance', min_value=1)
            st.number_input('How many years have you worked in this company', key='years_at_company', min_value=1, step=1)

                
        st.form_submit_button('Submit', on_click=make_prediction, kwargs=dict(pipeline=pipeline, encoder=encoder))


# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.warning('### Login from the Home page to use app')
else:
    if __name__ == "__main__":
        st.title("Make a Prediction")
        display_form()

        final_prediction = st.session_state["prediction"]
        probability = st.session_state["probability"]

        if not final_prediction:
            st.write("### Predictions show here ⬇️")
            st.divider()
        elif final_prediction == 'Yes':
            probability_of_yes = probability[0][1] * 100
            st.markdown(f"### Employee will leave 🏃‍♂️ IBM with a {round(probability_of_yes, 2)}% probability.")
            st.divider()
        else:
            probability_of_no = probability[0][0] * 100
            st.markdown(f"### Employee will stay 🧘‍♂️ at IBM with a {round(probability_of_no, 2)}% probability.")
            st.divider()

#     # st.write(st.session_state)





# # Initialise prediction in the session state
# if "prediction" not in st.session_state:
#     st.session_state['prediction'] = None

# # Initialise prediction in the session state
# if "pred_proba" not in st.session_state:
#     st.session_state['pred_proba'] = None




   

#     if not final_prediction:
#         st.write("### Predictions show here ⬇️")
#         st.divider()
#     elif final_prediction == 'Yes':
#         probability_of_yes = pred_proba[0][1] * 100
#         st.markdown(f"### Employee will leave 🏃‍♂️ IBM with a {round(probability_of_yes, 2)}% probability.")
#         st.divider()
#     else:
#         probability_of_no = pred_proba[0][0] * 100
#         st.markdown(f"### Employee will stay 🧘‍♂️ at IBM with a {round(probability_of_no, 2)}% probability.")
#         st.divider()
