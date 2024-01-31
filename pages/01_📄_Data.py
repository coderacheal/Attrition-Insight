import streamlit as st
import pandas as pd
import pyodbc


st.title('More about the Data')

# Initialize connection.
# Use st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

conn = init_connection()


@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
        
        #  Get column names
        columns = [column[0] for column in cur.description]

        # Convert rows to list of dictionaries
        data = [dict(zip(columns, row)) for row in rows]

        # Convert list of dictionaries to DataFrame
        df = pd.DataFrame(data)

        return df

data = run_query("SELECT * FROM LP2_Telco_churn_first_3000")
st.write(data)

# df = pd.json_normalize(df_com)
# st.write(df)


# for row in df_com:
#     st.write(type(row))
#     st.write(row)


# connection = pyodbc.connect(
#         "DRIVER={SQL Server};SERVER="
#         + st.secrets["server"]
#         + ";DATABASE="
#         + st.secrets["database"]
#         + ";UID="
#         + st.secrets["username"]
#         + ";PWD="
#         + st.secrets["password"]
#     )
# # Execute your SQL query
# cursor = connection.cursor()
# cursor.execute('SELECT * FROM LP2_Telco_churn_first_3000')

# # Fetch all rows
# rows = cursor.fetchall()

# # Get column names
# columns = [column[0] for column in cursor.description]

# # Convert rows to list of dictionaries
# data = [dict(zip(columns, row)) for row in rows]

# # Convert list of dictionaries to DataFrame
# df = pd.DataFrame(data)

# # Display DataFrame in Streamlit
# st.write(df)

# Close the cursor and connection
# cursor.close()
# conn.close()



# # Define column names
# columns = ['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
#        'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
#        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
#        'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
#        'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn']

# st.dataframe(df, columns=columns)


