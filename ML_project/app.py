import os
import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Get absolute paths to files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'cardio_model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'scaler.pkl')

model = None
scaler = None

def load_assets():
    global model, scaler
    print(f"Checking for model at: {MODEL_PATH}")
    print(f"Checking for scaler at: {SCALER_PATH}")
    
    if model is None and os.path.exists(MODEL_PATH):
        try:
            with open(MODEL_PATH, 'rb') as f:
                model = pickle.load(f)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            
    if scaler is None and os.path.exists(SCALER_PATH):
        try:
            with open(SCALER_PATH, 'rb') as f:
                scaler = pickle.load(f)
            print("Scaler loaded successfully.")
        except Exception as e:
            print(f"Error loading scaler: {e}")

@app.route('/')
def index():
    return render_template('index.html', active_page='home')

@app.route('/eda')
def eda():
    return render_template('eda.html', active_page='eda')

@app.route('/performance')
def performance():
    return render_template('performance.html', active_page='performance')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html', active_page='prediction')

@app.route('/predict', methods=['POST'])
def predict():
    load_assets()
    if model is None or scaler is None:
        return "Model or Scaler not loaded. Please ensure cardio_model.pkl and scaler.pkl exist.", 500

    try:
        # Extract inputs from form
        age = float(request.form.get('age', 0))
        gender = int(request.form.get('gender', 1))
        height = float(request.form.get('height', 0))
        weight = float(request.form.get('weight', 0))
        ap_hi = float(request.form.get('ap_hi', 0))
        ap_lo = float(request.form.get('ap_lo', 0))
        cholesterol = int(request.form.get('cholesterol', 1))
        gluc = int(request.form.get('gluc', 1))
        smoke = 1 if request.form.get('smoke') else 0
        alco = 1 if request.form.get('alco') else 0
        active = 1 if request.form.get('active') else 0

        # Preprocessing
        # 1. Age (The model was trained on ageInYr)
        ageInYr = age
        
        # 2. Blood Pressure Cleaning (Matching project.ipynb)
        if ap_hi < ap_lo:
            ap_hi, ap_lo = ap_lo, ap_hi
        
        # 3. BMI Calculation
        bmi = round(weight / ((height / 100) ** 2), 2) if height > 0 else 0

        # Feature vector in the exact order as trained:
        # gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, ageInYr, bmi
        features = np.array([[gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, ageInYr, bmi]])
        
        # Scaling
        features_scaled = scaler.transform(features)

        # Prediction
        prediction_val = model.predict(features_scaled)[0]
        probability_val = model.predict_proba(features_scaled)[0][1] * 100
        
        return render_template('result.html', 
                               prediction=int(prediction_val), 
                               probability=round(probability_val, 1))
    
    except Exception as e:
        return f"An error occurred during prediction: {str(e)}", 400

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

if __name__ == '__main__':
    print("Starting CardioCare Web Server...")
    app.run(debug=True)
