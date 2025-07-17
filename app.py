import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessors
model = joblib.load("supplier_model.pkl")
scaler = joblib.load("scaler (2).pkl")
numeric_cols = joblib.load("numeric_cols (2).pkl")
columns = joblib.load("columns.pkl")

# Title and intro
st.title("Supplier Reliability Predictor")
st.write("Enter the supplier details to predict reliability.")

# Create form input fields
input_data = {}
for col in columns:
    input_data[col] = st.text_input(f"{col}:", "")

# Submit button
if st.button("Predict Reliability"):
    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Convert numerical fields to float
    for col in numeric_cols:
        try:
            input_df[col] = input_df[col].astype(float)
        except:
            st.error(f"Please enter a valid number for {col}")
            st.stop()

    # Scale numerical fields
    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

    # Predict
    prediction = model.predict(input_df)

    # Show result
    if prediction[0] == 1:
        st.success("The supplier is predicted to be **reliable**.")
    else:
        st.warning("The supplier is predicted to be **not reliable**.")
