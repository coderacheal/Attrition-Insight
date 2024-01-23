import streamlit as st
import pandas as pd

import numpy as np

st.title('More about the Data')

data = pd.read_csv("vgsales.csv")

st.dataframe(data)
# st.table(data)
st.write(data)
