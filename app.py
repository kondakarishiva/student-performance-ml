import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("student_model.pkl", "rb"))

st.title("Student Performance Prediction")

study_hours = st.number_input("Study Hours")
attendance = st.number_input("Attendance (%)")
previous_marks = st.number_input("Previous Marks")

if st.button("Predict Result"):
    input_data = np.array([[study_hours, attendance, previous_marks]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Result: PASS ✅")
    else:
        st.error("Result: FAIL ❌")
