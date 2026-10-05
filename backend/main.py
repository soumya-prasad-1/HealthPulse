from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib

from backend.schemas import HealthData, WHORiskData
from backend.who_risk import calculate_who_risk


app = FastAPI(
    title="HealthPulse API",
    description="Smart Health Monitoring and Cardiovascular Prediction API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained ML model
model = joblib.load("ml/healthpulse_model.pkl")


@app.get("/")
def home():
    return {
        "message": "HealthPulse API is running successfully"
    }


@app.post("/predict")
def predict_health(data: HealthData):

    input_data = pd.DataFrame([{
        "age": data.age,
        "gender": data.gender,
        "height": data.height,
        "weight": data.weight,
        "ap_hi": data.ap_hi,
        "ap_lo": data.ap_lo,
        "cholesterol": data.cholesterol,
        "gluc": data.gluc,
        "smoke": data.smoke,
        "alco": data.alco,
        "active": data.active,
        "bmi": data.bmi
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "Cardiovascular Disease Predicted"
    else:
        result = "No Cardiovascular Disease Predicted"

    return {
        "prediction": int(prediction),
        "result": result,
        "message": "This prediction is for educational purposes only and is not a medical diagnosis."
    }
@app.post("/who-risk")
def who_risk(data: WHORiskData):

    try:

        result = calculate_who_risk(
            age=data.age,
            sex=data.sex,
            smoking=data.smoking,
            systolic_bp=data.systolic_bp,
            total_cholesterol=data.total_cholesterol,
            diabetes=data.diabetes
        )

        return {
            "success": True,
            "risk_percentage": result["risk_percentage"],
            "risk_category": result["risk_category"],
            "age_group": result["age_group"],
            "systolic_bp_group": result["systolic_bp_group"],
            "cholesterol_group": result["cholesterol_group"],
            "smoking_status": result["smoking_status"],
            "diabetes_status": result["diabetes_status"],
            "message": "This assessment is for educational purposes only and is not a medical diagnosis."
        }

    except ValueError as e:

        return {
            "success": False,
            "error": str(e)
        }