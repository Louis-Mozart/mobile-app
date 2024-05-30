import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create a synthetic dataset
data = {
    'age': np.random.randint(5, 80, 1000),
    'gender': np.random.choice(['male', 'female'], 1000)
}
df = pd.DataFrame(data)
df['height'] = df.apply(lambda row: (50 + 0.5 * row['age'] + (5 if row['gender'] == 'male' else 0) + np.random.randn()), axis=1)

# Convert gender to numeric values
df['gender'] = df['gender'].map({'male': 1, 'female': 0})

# Define features and target
X = df[['age', 'gender']]
y = df['height']

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model to a file
joblib.dump(model, 'height_model.pkl')
