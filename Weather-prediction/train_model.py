import pandas as pd
from sklearn.linear_model import Ridge
import joblib

# Load data
weather = pd.read_csv("weather.csv", index_col="DATE")

# Preprocessing
null_pct = weather.apply(pd.isnull).sum()/weather.shape[0]
valid_columns = weather.columns[null_pct < .05]
weather = weather[valid_columns].copy()
weather.columns = [c.lower() for c in weather.columns]
weather = weather.ffill()

# Create target
weather["target"] = weather.shift(-1)["tmax"]
weather = weather.ffill()

# Define predictors
predictors = weather.columns[~weather.columns.isin(["target", "name", "station"])]

# Initialize and train the model
rr = Ridge(alpha=.1)
rr.fit(weather[predictors], weather["target"])

# Save the model and predictors
joblib.dump(rr, 'model.pkl')
joblib.dump(predictors, 'predictors.pkl')

print("Model and predictors trained and saved.")
