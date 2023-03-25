import streamlit as st
import eda
import BestRandomForestModel

# Create navigation function
navigation = st.sidebar.selectbox('Pilih Halaman : ', ('EDA', 'Data Prediction'))

if navigation == 'EDA':
    eda.run()
else:
    BestRandomForestModel.run()