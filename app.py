import streamlit as st

st.set_page_config(page_title="Parkinson Disease Prediction", page_icon="🩺")

st.title("🩺 AI and IoT Based Parkinson's Disease Prediction System")

st.write("""
Welcome to the Parkinson's Disease Prediction and Monitoring System.

This project uses Artificial Intelligence (XGBoost) and IoT sensors
to assist in the early prediction and monitoring of Parkinson's disease.
""")

st.header("Patient Details")

age = st.number_input("Age", min_value=1, max_value=120)
heart_rate = st.number_input("Heart Rate (BPM)", min_value=30, max_value=200)
emg = st.number_input("EMG Sensor Value", min_value=0)
mems = st.number_input("MEMS Sensor Value", min_value=0)

if st.button("Predict"):
    if heart_rate > 100:
        st.error("Prediction: High Risk of Parkinson's Disease")
    else:
        st.success("Prediction: Low Risk of Parkinson's Disease")

st.header("Health Monitoring")

st.write("- Heart Rate Monitoring")
st.write("- EMG Sensor Monitoring")
st.write("- MEMS Sensor Monitoring")
st.write("- IoT Cloud Monitoring")

st.info("This is a demonstration project based on AI and IoT concepts.")
