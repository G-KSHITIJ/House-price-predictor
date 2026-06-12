import streamlit as st
import pickle
import numpy as np

# Load model
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 House Price Predictor")

CRIM = st.number_input("Crime Rate")
ZN = st.number_input("Residential Land")
INDUS = st.number_input("Industry Area")
CHAS = st.number_input("Charles River (0 or 1)")
NOX = st.number_input("NOX Pollution")
RM = st.number_input("Number of Rooms")
AGE = st.number_input("Age")
DIS = st.number_input("Distance")
RAD = st.number_input("Highway Access")
TAX = st.number_input("Tax Rate")
PTRATIO = st.number_input("Pupil Teacher Ratio")
B = st.number_input("B")
LSTAT = st.number_input("Lower Status Population")

if st.button("Predict Price"):
    features = np.array([[CRIM, ZN, INDUS, CHAS, NOX,
                          RM, AGE, DIS, RAD,
                          TAX, PTRATIO, B, LSTAT]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ${prediction[0]*1000:,.2f}")