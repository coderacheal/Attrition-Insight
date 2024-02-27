import streamlit as st

feature_descriptions = """

1. **Age**: Age of employee
2. **Attrition**: Employee attrition status
3. **Department**: Department of work
4. **DistanceFromHome**: what is their distance from hime
5. **Education**: 1-Below College; 2- College; 3-Bachelor; 4-Master; 5-Doctor;
6. **EducationField**: The field they studies in in the University
7. **EnvironmentSatisfaction**: 1-Low; 2-Medium; 3-High; 4-Very High;
8. **JobSatisfaction**: 1-Low; 2-Medium; 3-High; 4-Very High;
9. **MaritalStatus**: Whether they are married, single or divorced
10. **MonthlyIncome**: How much an employee makes a month
11. **NumCompaniesWorked**: Number of companies worked prior to IBM
12. **WorkLifeBalance**: 1-Bad; 2-Good; 3-Better; 4-Best;
13. **YearsAtCompany**: Current years of service in IBM

"""

column_1 = """
### Attrition Insight
Attrition Insight is a Machine Learning application that  predicts the likelihood of an employee to leave the company based on various demographic and job-related factors.

### Key Features
- **View Data:** Access proprietory data from IBM.
- **Dashboard:** Explore interactive data visualizations for insights.
- **Real-time Prediction:** Instantly see predictions for employee attrition.
- **History:** See past predictions made.

### User Benefits
- **Data-driven Decisions:** Make informed decisions backed by data analytics.
- **Easy Machine Learning:** Utilize powerful machine learning algorithms effortlessly.
- **Live Demo:** Watch a demo video to see the app in action.

[Watch Demo Video](link)
"""

column_2 = """
### Machine Learning Integration
- **Model Selection:** Choose between two advanced models for accurate predictions.
- **Seamless Integration:** Integrate predictions into your workflow with a user-friendly interface.
- **Probability Estimates:** Gain insights into the likelihood of predicted outcomes.

### Need Help?
For collaborations contact me at [hello@rachealappiahkubi.com](mailto:hello@rachealappiahkubi.com).
"""


#Build command
# mkdir .streamlit; cp /etc/secrets/secrets.toml ./.streamlit/; pip install --upgrade pip && pip install -r requirements.txt