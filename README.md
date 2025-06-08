# 🔋 Battery Temperature Forecasting Web App

**Forecast future battery temperature trends over upcoming charge/discharge cycles using Machine Learning + Flask + Chart.js.**



## 📌 Project Overview

This project implements an end-to-end ML pipeline and interactive web app to:

✅ Analyze **NASA B0005 battery dataset**.

✅ Train a **Linear Regression** model for **time series forecasting**.

✅ Deploy the model via a **Flask REST API**.

✅ Build a simple **UI Dashboard** with **Chart.js** for visualization.

✅ Allow user to input temperature value and forecast next **50 future cycles**.



## 🚗 Why Battery Temperature Matters

* Battery temperature affects **capacity fade**, **thermal degradation**, and **safety**.
* Accurate forecasting can improve:

  * Battery life cycle management
  * Thermal control system optimization
  * EV reliability & efficiency



## 🗂 Directory Structure

```
Battery_forecast/
│
├── model/
│   ├── battery_temp_model.pkl      # Trained Linear Regression model
│   ├── scaler.pkl                  # Fitted MinMaxScaler
│
├── static/
│   └── index.html                  # Interactive UI (Chart.js + HTML + JS)
│
├── app.py                          # Flask REST API
│
├── B0005_discharge.csv              # NASA Battery Dataset (discharge cycles)
│
├── requirements.txt                # Project dependencies
│
└── README.md                       # Project documentation
```



## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com//Battery_forecast.git
cd Battery_forecast
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train and Save Model (Optional)

If not already trained, run the model training script (`train_model.py` or inside a notebook):

```bash
python train_model.py
```

Or use the provided `battery_temp_model.pkl` and `scaler.pkl`.

### 4️⃣ Run the Flask App

```bash
python app.py
```

### 5️⃣ Open Web App

Go to:

```
http://127.0.0.1:5000
```



## ⚙️ How It Works

* User inputs a **starting temperature** value in UI.
* The app sends this value to `/predict` endpoint via POST request.
* Flask API uses **Linear Regression model** to forecast **next 50 cycle temperatures**.
* Forecasted temperatures are returned as JSON.
* UI displays the result as an interactive **line chart** using **Chart.js**.



## 🛠 Technologies Used

✅ Python
✅ Flask
✅ Scikit-learn
✅ Pandas / Numpy
✅ MinMaxScaler
✅ Chart.js
✅ HTML + JavaScript



## 🚧 Future Work

* I am working on implementing **LSTM / GRU** for more advanced time series forecasting
* Adding **Voltage** and **Current** multivariate forecasting
* Will deploy on **Heroku / AWS / Render**
* Improving UI (Bootstrap / React)
* Adding real-time data streaming support



## 📚 Dataset Reference

* NASA Ames Prognostics Data Repository
  [https://www.nasa.gov/content/prognostics-center-of-excellence-data-set-repository](https://www.nasa.gov/content/prognostics-center-of-excellence-data-set-repository)

Dataset: **B0005 Battery aging dataset**

---

## ✨ Example Result

<img width="584" alt="demo_battery" src="https://github.com/user-attachments/assets/7dac06cd-21f8-46e0-9111-8fa9373e832f" />


---



**If you like this project, give it a ⭐️ on GitHub! 🚀**

