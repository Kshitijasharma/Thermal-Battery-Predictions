import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import pickle

# Load and preprocess
df = pd.read_csv('B0005_discharge.csv')
df = df[['id_cycle', 'Temperature_measured']].dropna()
temp_series = df.groupby('id_cycle')['Temperature_measured'].mean().values.reshape(-1, 1)

# Scaling
scaler = MinMaxScaler()
scaled = scaler.fit_transform(temp_series)

# Create sequences
X, y = [], []
window_size = 10
for i in range(len(scaled) - window_size):
    X.append(scaled[i:i+window_size].flatten())
    y.append(scaled[i+window_size])
X, y = np.array(X), np.array(y)

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model and scaler
with open("model.pkl", "wb") as f: pickle.dump(model, f)
with open("scaler.pkl", "wb") as f: pickle.dump(scaler, f)
