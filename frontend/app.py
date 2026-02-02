import sys
import os
import streamlit as st

# ===========================
# Backend import (no __init__.py needed)
# ===========================
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend'))
)
from model import predict

# ===========================
# Page Config
# ===========================
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📊",
    layout="centered"
)

# ===========================
# App Header
# ===========================
st.markdown(
    """
    <h1 style='text-align: center;'>📊 Student Performance Predictor</h1>
    <p style='text-align: center; font-size: 16px;'>
    Predict a student's <b>Performance Index</b> using academic and lifestyle factors.
    </p>
    """,
    unsafe_allow_html=True
)

st.caption(
    "This model uses study habits, sleep patterns, and academic history "
    "to estimate performance."
)

st.divider()

# ===========================
# Sidebar Inputs
# ===========================
st.sidebar.header("🧮 Input Features")

hours_studied = st.sidebar.slider(
    "Hours Studied per Day", 0.0, 20.0, 5.0, 0.5
)

previous_scores = st.sidebar.slider(
    "Previous Academic Score", 0.0, 100.0, 50.0, 1.0
)

extracurricular = st.sidebar.radio(
    "Extracurricular Activities", ["No", "Yes"]
)

sleep_hours = st.sidebar.slider(
    "Sleep Hours per Day", 0.0, 12.0, 7.0, 0.5
)

sample_questions = st.sidebar.number_input(
    "Sample Question Papers Practiced", 0, 50, 10
)

extracurricular_val = 1 if extracurricular == "Yes" else 0

features = [
    float(hours_studied),
    float(previous_scores),
    float(extracurricular_val),
    float(sleep_hours),
    float(sample_questions)
]

# ===========================
# Input Summary
# ===========================
st.subheader("📌 Selected Inputs")

with st.container(border=True):
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Hours Studied:** {hours_studied}")
        st.write(f"**Previous Score:** {previous_scores}")
        st.write(f"**Extracurricular:** {extracurricular}")

    with col2:
        st.write(f"**Sleep Hours:** {sleep_hours}")
        st.write(f"**Sample Papers Practiced:** {sample_questions}")

st.divider()

# ===========================
# Prediction
# ===========================
if st.button("🔮 Predict Performance", use_container_width=True):
    try:
        with st.spinner("Predicting performance..."):
            prediction = float(predict(features))

        st.success("Prediction Successful ✅")

        st.metric(
            label="📈 Predicted Performance Index",
            value=f"{prediction:.2f}"
        )

        st.info(
            "💡 Consistent study hours, proper sleep, and regular practice "
            "can significantly improve academic performance."
        )

    except Exception as e:
        st.error("❌ Prediction failed")
        st.exception(e)

# ===========================
# Footer
# ===========================
st.divider()
st.markdown(
    "<p style='text-align:center; font-size:12px;'>"
    "Built with ❤️ using Scikit-Learn & Streamlit | Deployed on Render"
    "</p>",
    unsafe_allow_html=True
)
