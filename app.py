import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model and other artifacts
model = pickle.load(open('supplier_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))
numeric_cols = pickle.load(open('numeric_cols (2).pkl', 'rb'))  # Use the correct renamed file

# Title
st.title("Supplier Reliability Predictor")
st.write("Enter the supplier details to predict reliability.")

# Input fields
quantity = st.number_input("Quantity:", min_value=0.0, format="%.2f")
unit_price = st.number_input("Unit Price:", min_value=0.0, format="%.2f")
negotiated_price = st.number_input("Negotiated Price:", min_value=0.0, format="%.2f")
defective_units = st.number_input("Defective Units:", min_value=0.0, format="%.2f")
delivery_days = st.number_input("Delivery Days:", min_value=0.0, format="%.2f")

supplier = st.selectbox("Supplier:", ['Alpha Corp', 'Beta Supplies', 'Gamma Co', 'Delta Logistics', 'Epsilon Group'])
item_category = st.selectbox("Item Category:", ['Office Supplies', 'Raw Materials', 'MRO', 'Packaging'])
order_status = st.selectbox("Order Status:", ['Delivered', 'Pending', 'Partially Delivered'])
compliance = st.radio("Compliance:", ['Yes', 'No'])

if st.button("Predict"):
    # Create input dictionary
    input_dict = {
        'Quantity': quantity,
        'Unit_Price': unit_price,
        'Negotiated_Price': negotiated_price,
        'Defective_Units': defective_units,
        'Delivery_Days': delivery_days,
        'Supplier_' + supplier.replace(" ", "_"): 1,
        'Item_Category_' + item_category.replace(" ", "_"): 1,
        'Order_Status_' + order_status.replace(" ", "_"): 1,
        'Compliance_Yes': 1 if compliance == 'Yes' else 0
    }

    # Add missing categorical columns as 0
    for col in columns:
        if col not in input_dict:
            input_dict[col] = 0

    # Create input dataframe
    input_df = pd.DataFrame([input_dict])

    # Ensure all numeric columns are present
    missing_num_cols = [col for col in numeric_cols if col not in input_df.columns]
    if missing_num_cols:
        st.error(f"Error: Missing numeric columns in input: {missing_num_cols}")
    else:
        # Scale numeric features
        input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

        # Reorder columns to match training
        input_df = input_df[columns]

        # Predict
        prediction = model.predict(input_df)[0]
        if prediction == 1:
            st.success("✅ The supplier is predicted to be RELIABLE.")
        else:
            st.warning("⚠️ The supplier is predicted to be NOT RELIABLE.")
