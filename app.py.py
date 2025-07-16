import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model and preprocessing objects
model = joblib.load("supplier_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# Set up the Streamlit interface
st.set_page_config(page_title="Supplier Delivery Predictor", layout="centered")
st.title("📦 Supplier Reliability Predictor")
st.markdown("Predict whether a delivery will be **Late** or **On-Time** based on supplier details.")

# Input form
with st.form("input_form"):
    quantity = st.number_input("Quantity", min_value=1, value=100)
    unit_price = st.number_input("Unit Price", min_value=0.0, value=50.0)
    negotiated_price = st.number_input("Negotiated Price", min_value=0.0, value=45.0)
    defective_units = st.number_input("Defective Units", min_value=0, value=2)

    item_category = st.selectbox("Item Category", ["MRO", "Office Supplies", "Raw Materials"])
    order_status = st.selectbox("Order Status", ["Delivered", "Pending", "Cancelled"])
    compliance = st.selectbox("Compliance", ["Yes", "No"])

    submitted = st.form_submit_button("Predict")

# When submitted
if submitted:
    # Manual one-hot encoding
    input_dict = {
        'Quantity': quantity,
        'Unit_Price': unit_price,
        'Negotiated_Price': negotiated_price,
        'Defective_Units': defective_units,
        'Item_Category_MRO': 1 if item_category == "MRO" else 0,
        'Item_Category_Office Supplies': 1 if item_category == "Office Supplies" else 0,
        'Item_Category_Raw Materials': 1 if item_category == "Raw Materials" else 0,
        'Order_Status_Delivered': 1 if order_status == "Delivered" else 0,
        'Order_Status_Pending': 1 if order_status == "Pending" else 0,
        'Order_Status_Cancelled': 1 if order_status == "Cancelled" else 0,
        'Compliance_Yes': 1 if compliance == "Yes" else 0,
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Add missing columns (if any) and reorder
    for col in columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[columns]

    # Scale numeric features
    num_cols = ['Quantity', 'Unit_Price', 'Negotiated_Price', 'Defective_Units']
    input_df[num_cols] = scaler.transform(input_df[num_cols])

    # Make prediction
    prediction = model.predict(input_df)[0]
    result = "🚚 **Late Delivery**" if prediction == 1 else "✅ **On-Time Delivery**"
    st.success(f"Prediction: {result}")
