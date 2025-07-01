# Weather Prediction Streamlit App

This project is a Streamlit web application that predicts the next day's maximum temperature based on historical weather data.

## Project Structure

```
.
├── app.py              # Main Streamlit application
├── model.pkl           # Trained machine learning model
├── predictors.pkl      # List of features used by the model
├── README.md           # Project readme
├── requirements.txt    # Python dependencies
├── train_model.py      # Script to train the model
└── weather.csv         # Raw weather data
```

## Local Setup

### Installation

To run this project, please install the following:

*   Python 3.8+
*   The packages in `requirements.txt`.

You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

### Data

The `weather.csv` dataset was downloaded from [NOAA](https://www.ncdc.noaa.gov/cdo-web/search). It contains daily weather data for JFK International Airport in New York.

### Model Training

To train the model from scratch, run the following command:

```bash
python train_model.py
```

This will generate `model.pkl` and `predictors.pkl`.

## Running the Application

To start the Streamlit application, run the following command in your terminal:

```bash
streamlit run app.py
```

You can then view the application in your browser at `http://localhost:8501`.