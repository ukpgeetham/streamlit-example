import pandas as pd
import streamlit as st
import xlwings as xw

global dataframe
uploaded_file = st.file_uploader(label="Upload your CSV or Excel a file",type=['csv','xlsx'])
if uploaded_file is not None:
    try:
        dataframe = pd.read_csv(uploaded_file)
    except Exception as e:
        dataframe = xw.Book(uploaded_file)
st.write(dataframe)
