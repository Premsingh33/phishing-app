# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import joblib
import os

# ✅ Load model from the same folder
model_path = os.path.join(os.path.dirname(__file__), "phishing_model.pkl")
model = joblib.load(model_path)

# Streamlit App
st.title("🛡️ Phishing Website Detection App")
st.write("Enter website-related features to check if it's Legit or Phishing.")

# Input features
def get_user_input():
    length_url = st.number_input("Length of URL", min_value=0)
    nb_dots = st.number_input("Number of Dots", min_value=0)
    nb_hyphens = st.number_input("Number of Hyphens", min_value=0)
    nb_at = st.number_input("Number of @ Symbols", min_value=0)
    nb_qm = st.number_input("Number of ? Symbols", min_value=0)
    # Add more inputs as needed...

    data = {
        'length_url': length_url,
        'nb_dots': nb_dots,
        'nb_hyphens': nb_hyphens,
        'nb_at': nb_at,
        'nb_qm': nb_qm,
        # Add other required keys here
    }

    return pd.DataFrame([data])

# Get user input
input_df = get_user_input()

# Predict
if st.button("🔍 Check"):
    prediction = model.predict(input_df)[0]
    if prediction == 0:
        st.success("🟢 Legitimate Website")
    else:
        st.error("🔴 Phishing Website")
