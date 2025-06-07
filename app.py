from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load model & scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    start_temp = float(data['temperature'])

    # Start sequence with scaled user input
    start_scaled = scaler.transform([[start_temp]])
    seed_seq = np.repeat(start_scaled, 10).reshape(1, -1)  # repeat to match window_size=10

    predictions = []
    for _ in range(50):
        pred_scaled = model.predict(seed_seq)[0]
        predictions.append(pred_scaled)
        seed_seq = np.append(seed_seq[:, 1:], pred_scaled.reshape(1, 1), axis=1)


    # Inverse transform
    predicted_temps = scaler.inverse_transform(np.array(predictions).reshape(-1, 1)).flatten()

    return jsonify({'predicted_temperatures': predicted_temps.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
