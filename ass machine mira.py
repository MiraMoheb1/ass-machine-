import streamlit as st 
import pickle
import pandas as pd 
import sklearn

st.title('Heart disease')
st.info('Heart disease prediction ')
st.sidebar.header('Feature Selection')

Age=st.text_input('age')
Sex=st.text_input('sex')
Chest_pain_type=st.text_input('Chest Pain Type')
Resting_blood_pressure =st.text_input('Resting Blood Pressure')
Serum_cholesterol_level =st.text_input('Serum Cholesterol Level')
Fasting_blood_sugar =st.text_input('Fasting Blood Sugar')
Resting_electrocardiographic_results =st.text_input('Resting Electrocardiographic Results')
Maximum_heart_rate_achieved =st.text_input('Maximum Heart Rate Achieved')
Exercise_induced_angina =st.text_input('Exercise Induced angina')
ST_depression_induced_by_exercise_relative_to_rest =st.text_input('ST Depression Induced By Exercise Relative To Rest')
Slope_of_the_peak_exercise_segment =st.text_input('Slope Of The Peak Exercise Segment')
Number_of_major_vessels_colored_by_fluoroscopy =st.text_input('Number Of Major Vessels Colored By Fluoroscopy')
Thalassemia_type =st.text_input('Thalassemia Type ')