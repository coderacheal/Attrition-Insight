import streamlit as st

feature_descriptions = """

The following describes the columns present in the data.
**Gender** Whether the customer is a male or a female*

**SeniorCitizen** -- *Whether a customer is a senior citizen or not*

**Partner** -- *Whether the customer has a partner or not (Yes, No)*

**Dependents** -- *Whether the customer has dependents or not (Yes, No)*

**Tenure** -- *Number of months the customer has stayed with the company*

**Phone Service** -- *Whether the customer has a phone service or not (Yes, No)*

**MultipleLines** -- *Whether the customer has multiple lines or not*

**InternetService** -- *Customer's internet service provider (DSL, Fiber Optic, No)*

**OnlineSecurity** -- *Whether the customer has online security or not (Yes, No, No Internet)*

**OnlineBackup** -- *Whether the customer has online backup or not (Yes, No, No Internet)*

**DeviceProtection** -- *Whether the customer has device protection or not (Yes, No, No internet service)*

**TechSupport** -- *Whether the customer has tech support or not (Yes, No, No internet)*

**StreamingTV** -- *Whether the customer has streaming TV or not (Yes, No, No internet service)*

**StreamingMovies** -- *Whether the customer has streaming movies or not (Yes, No, No Internet service)*

**Contract** -- *The contract term of the customer (Month-to-Month, One year, Two year)*

**PaperlessBilling** -- *Whether the customer has paperless billing or not (Yes, No)*

**Payment Method** -- *The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))*

**MonthlyCharges** -- *The amount charged to the customer monthly*

**TotalCharges** -- *The total amount charged to the customer*

**Churn&& -- *Whether the customer churned or not (Yes or No)*
"""



column_1 = f"""
    # Attrition Meter
    This app show where or not an employee will leave the company not based on certain determined demographics and job related questions
    ## Key Features
    - Dashboard - Contains Data Visualization
    - Predict - Allows you to view prediction in real time
    ## User Benefits
    - Make data-driven decisions effortlessly.
    - Harness the power of machine learning without the complexity.
    ## Live Demo
    [Watch Demo Video](link) or [Get Started Now](link)
   
"""

column_2 = """
    ## Machine Learning Integration
    - You have access to select between 2 models for prediction
    - Simple integration and user-friendly interface.
    ## Advanced Features
    - Customization options for model parameters.
    - Real-time predictions for up-to-the-minute insights.
    ## About
    Attrition Meter is developed by a passionate team of data scientists and engineers dedicated to simplifying data analysis and machine learning.
    ## Need Help?
    Contact us at  hello@rachealappiahkubi.com
    © 2024. All rights reserved.
    """

# st.link_button('GitHub', url='https://github.com/coderacheal')
# st.link_button('Medium', url='https://medium.com/coderacheal')
