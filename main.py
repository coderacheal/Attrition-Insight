import streamlit as st
import pandas as pd

import numpy as np

st.title('Attrition Meter')

name = st.text_input('Enter your name: ')
st.write(f"Hello {name}")

data = pd.read_csv("vgsales.csv")
st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)


st.bar_chart(chart_data)
st.line_chart(chart_data)



print(name)

