import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(
    page_title="Fraud Detection App",
    page_icon="💳",
    layout="centered"
)

# Load trained model
try:
    model = joblib.load("fraud_detection_pipeline.pkl")
except FileNotFoundError:
    st.error("⚠️ Model file 'fraud_detection_pipeline.pkl' not found.")
    st.info("Please make sure the model file is in the same folder as app.py")
    st.stop()

# App Title
st.title("💳 Fraud Detection Prediction App")

st.markdown(
    "Enter the transaction details below and click **Predict** to check whether the transaction is fraudulent."
)

st.divider()

# -------------------------
# User Inputs
# -------------------------

transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"]
)

amount = st.number_input("Amount", min_value=0.0, value=1000.0)

oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)

newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)

oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)

newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

# -------------------------
# Prediction
# -------------------------

if st.button("Predict"):
    try:
        input_data = pd.DataFrame({
            "type": [transaction_type],
            "amount": [amount],
            "oldbalanceOrg": [oldbalanceOrg],
            "newbalanceOrig": [newbalanceOrig],
            "oldbalanceDest": [oldbalanceDest],
            "newbalanceDest": [newbalanceDest]
        })

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.error("🚨 Fraudulent Transaction Detected!")
        else:
            st.success("✅ Transaction is NOT Fraudulent")

    except Exception as e:
        st.error("❌ Error during prediction")
        st.write(e)


# to run the app, use the command:
# python -m streamlit run app.py
