import numpy as np
import joblib
import streamlit as st

obj=joblib.load('california.joblib')
model=obj['model']
cols=obj['columns']

st.title('California Housing Price Prediction')
In=[]
for i in cols:
    v=st.number_input(f'Enter {i} value:')
    In.append(v)
if st.button('click'):
    out=model.predict([In])
    st.success(f'The median house value is {out}')
