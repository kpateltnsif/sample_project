import streamlit as st
import sys
import os

# Add backend folder to path dynamically (no __init__.py needed)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from model import predict

# ===========================
# Streamlit App
# ===========================
st.title("Student Performance Predictor")
st.write("Predict the Performance Index of a student based on input features.")

# User input
hours_studied = st.number_input("Hours Studied", min_value=0.0, max_value=20.0, value=5.0)
previous_scores = st.number_input("Previous Scores", min_value=0.0, max_value=100.0, value=50.0)
extracurricular = st.selectbox("Extracurricular Activities", ["No", "Yes"])
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=12.0, value=7.0)
sample_questions = st.number_input("Sample Question Papers Practiced", min_value=0, max_value=50, value=10)

# Convert categorical input
extracurricular_val = 1 if extracurricular == "Yes" else 0

# Prepare feature list
features = [
    float(hours_studied),
    float(previous_scores),
    float(extracurricular_val),
    float(sleep_hours),
    float(sample_questions)
]

# Prediction button
if st.button("Predict"):
    try:
        prediction = predict(features)
        st.success(f"Predicted Performance Index: {prediction:.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
