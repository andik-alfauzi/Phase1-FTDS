import numpy as np
import pandas as pd
import streamlit as st
import pickle

# load the model 
with open('BestRandomForestModel.pkl', 'rb') as file1:
  randForBestEstGS = pickle.load(file1)

def run():
    
    def age_bin(age):
      if age > 15 and age < 25:
        return 'teen'
      elif age >= 25 and age < 55:
        return 'adult'
      else:
        return 'old'

  # membuat input data baru
    with st.form(key='heart_failure_form'):
      age = st.number_input('age', min_value=15, max_value=120, value=20, step=1, help='Usia Customer')
      sex = st.selectbox('sex', ('Female', 'Male'))
      bmi = st.number_input('bmi', min_value=0.00, step=0.01, value=0.00, format='%.2g')
      children =  st.number_input('children', min_value=0, max_value=20, value=0)
      smoker = st.selectbox('smoker', ('No', 'Yes'))
      region = st.selectbox('region', ('Southwest', 'Southeast', 'Northwest', 'Northeast'))
      st.markdown('---')
      
      binAge = age_bin(age)
      
      submitted = st.form_submit_button('Predict')
        
    infData = {
      'age_bin' : binAge,
      'sex' : sex,
      'bmi' : bmi,
      'children' : children,
      'smoker' : smoker,
    }

    infData = pd.DataFrame([infData])
    st.dataframe(infData)

    # Buat function di column submitted
    if submitted:

        # Predict using Random Forest Regressor with Grid Search Tuning
        y_predInfData = randForBestEstGS.predict(infData)
        st.write('Charges Prediction : ', str(int(y_predInfData)))

if __name__ == '__main__':
   run()