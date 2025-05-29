import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split

# RandomForest: Machine Learning Model
from sklearn.ensemble import RandomForestRegressor

# Creating a Navigation Bar
nav = st.sidebar.radio("Navigation", ["About", "Predict"])

# Reading the Dataset,
df = pd.read_csv(r"C:\Users\Sheewakoti-Manish\Documents\My-Codes\Insurance-Premium-Prediction\insurance.csv")

if nav == "About":
    st.title("Health Insurance Premium Predictor")
    st.text("")
    st.text("")
    # Adding Images in About Section
    st.image(r"C:\Users\Sheewakoti-Manish\Documents\My-Codes\Insurance-Premium-Prediction\health_insurance.jpeg", width = 600)

# Feature Encoding 
df.replace({"sex": {"male": 0, "female": 1}}, inplace = True)
df.replace({"smoker": {"yes": 0, "no": 1}}, inplace = True)
df.replace({"region": {"southeast": 0, "southwest": 1, "northeast": 2, "northwest": 3}}, inplace = True)

# Dropping Charges
# This is an Independent Feature, in X
x = df.drop(columns = "charges", axis = 1)
# Target Variable of Charges...
y = df["charges"]

# Creating up an Instance of a Random Forest Regressor, 
rfr = RandomForestRegressor()
# Training the Model
rfr.fit(x, y)   # calling the fit method

if nav == "Predict":
    st.title("Enter Details: ")

    # Receiving out the input for each
    age = st.number_input("Age: ", step = 1, min_value = 0)

    sex = st.radio("Sex ", ("Male", "Female"))

    if (sex == "Male"):
        s =  0
    if (sex == "Female"):
        s = 1
    bmi = st.number_input("BMI: ", min_value = 0 )

    children = st.number_input("Number of Children: ", step = 1, min_value = 0 )

    smoke = st.radio("Do you Smoke?", ("Yes", "No"))

    if (smoke == "Yes"):
        sm = 0
    if (smoke == "No"):
        sm = 1

    region = st.selectbox("Region", ("SouthEast", "SouthWest", "NorthEast", "NorthWest"))

    if (region == "SouthEast"):
        reg = 0
    if (region == "SouthWest"):
        reg = 1
    if (region == "NorthEast"):
        reg = 2
    if (region == "NorthWest"):
        reg = 3
    
    if st.button ("Predict"):
        st.subheader("Predicted Premium")
        st.text(rfr.predict([[age, s, bmi, children, sm, reg]]))
    