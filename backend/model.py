import joblib
import numpy as np

# Load the trained model
model = joblib.load('height_model.pkl')

def predict(age, gender):
    # Convert gender to numeric value
    gender = 1 if gender.lower() == 'male' else 0
    # Create feature array
    features = np.array([[age, gender]])
    prediction = model.predict(features)
    return float(prediction[0])
