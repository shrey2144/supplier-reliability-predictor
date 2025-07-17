import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessors
model = joblib.load("supplier_model.pkl")
scaler = joblib.load("scaler (2).pkl")
numeric_cols = joblib.load("numeric_cols (2).pkl")
all_columns = joblib.load("columns.pkl")

# Define category options based on dummy columns
supplier_options = ['Beta Supplies', 'Delta Logistics', 'Epsilon Group', 'Gamma Co']
item_category_options = ['MRO', 'Office Supplies', 'Packaging', 'Raw Materials']
order_status_options = ['Delivered', 'Partially Delivered', 'Pending']
compliance_options = ['Yes', 'No']

# App title
st.title("Supplier Reliability Predictor")
st.write("Enter the supplier details to predict reliability.")

# Form inputs
quantity = st.number_input("Quantity:", min_value=0.0)
unit_price = st.number_input("Unit Price:", min_value=0.0)
negotiated_price = st.number_input("Negotiated Price:", min_value=0.0)
defective_units = st.number_input("Defective Units:", min_value=0.0)

supplier = st.selectbox("Supplier:", supplier_options)
category = st.selectbox("Item Category:", item_category_options)
order_status = st.selectbox("Order Status:", order_status_options)
compliance = st.radio("Compliance:", compliance_options)

# Submit button
if st.button("Predict Reliability"):
    # Start input dict
    input_data = {
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Negotiated_Price": negotiated_price,
        "Defective_Units": defective_units,
    }

    # Add one-hot encoded fields
    for s in supplier_options:
        input_data[f"Supplier_{s}"] = 1 if supplier == s else 0
    for cat in item_category_options:
        input_data[f"Item_Category_{cat}"] = 1 if category == cat else 0
    for status in order_status_options:
        input_data[f"Order_Status_{status}"] = 1 if order_status == status else 0

    input_data["Compliance_Yes"] = 1 if compliance == "Yes" else 0

    # Convert to DataFrame and align with expected columns
    input_df = pd.DataFrame([input_data])
    for col in all_columns:
        if col not in input_df.columns:
            input_df[col] = 0  # fill missing dummy columns

    input_df = input_df[all_columns]  # reorder columns

    # Scale numeric values
    # Fix: ensure all numeric columns exist
    missing_numeric = [col for col in numeric_cols if col not in input_df.columns]
    
    if missing_numeric:
        st.error(f"❌ Error: Missing numeric columns in input: {missing_numeric}")
    else:
        input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

    # Predict
    prediction = model.predict(input_df)

    # Result
    if prediction[0] == 1:
        st.success("✅ The supplier is predicted to be **RELIABLE**.")
    else:
        st.error("⚠️ The supplier is predicted to be **NOT RELIABLE**.")
