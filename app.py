import streamlit as st
import pandas as pd

st.title("Unbiased AI Decision System")

# User Input
gender = st.selectbox("Gender", ["Male", "Female"])
income = st.slider("Income", 10000, 100000, 30000)
score = st.slider("Credit Score", 300, 900, 600)

# Biased Model (example)
if gender == "Male" and income > 30000:
    decision = "Approved"
else:
    decision = "Rejected"

# Fairness Correction
if income > 30000 and score > 600:
    fair_decision = "Approved"
else:
    fair_decision = "Rejected"

# Output
st.subheader("Biased AI Decision:")
st.write(decision)

st.subheader("Fair AI Decision:")
st.write(fair_decision)

st.info("This shows how bias can affect decisions and how fairness improves it.")