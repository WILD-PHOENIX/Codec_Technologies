import streamlit as st
import pandas as pd
import joblib

# Load the weather data
@st.cache_data
def load_data():
    data = pd.read_csv('weather.csv')
    return data

# Load the trained model and predictors
model = joblib.load('model.pkl')
predictors = joblib.load('predictors.pkl')

data = load_data()

st.title("Next Day's Max Temperature Predictor")

st.write("Enter the weather conditions to predict the next day's maximum temperature.")

# Create input fields for user
input_data = {}
for predictor in predictors:
    if predictor in ['tmin', 'tmax']:
        input_data[predictor] = st.slider(f'{predictor.upper()} (Temperature)', -20, 120, 50)
    elif predictor == 'prcp':
        input_data[predictor] = st.slider(f'{predictor.upper()} (Precipitation)', 0.0, 5.0, 0.1, 0.01)
    elif predictor == 'snow':
        input_data[predictor] = st.slider(f'{predictor.upper()} (Snow)', 0.0, 20.0, 0.0, 0.1)
    elif predictor == 'snwd':
        input_data[predictor] = st.slider(f'{predictor.upper()} (Snow Depth)', 0.0, 40.0, 0.0, 0.1)

# Prediction button
if st.button("Predict"):
    # Create a DataFrame from the user inputs
    input_df = pd.DataFrame([input_data])
    input_df = input_df[predictors] # Ensure correct order

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Display the prediction
    st.success(f"The predicted maximum temperature for the next day is: {prediction:.2f}°F")

st.write("Here's the raw data:")
st.write(data.head())
