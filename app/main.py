from fastapi import FastAPI

from app.schemas import PatientData
from app.predictor import predict_heart_disease
from app.risk_analyzer import get_risk_level
from app.recommendations import (
    get_recommendations,
    get_patient_specific_advice
)


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Heart AI API is running!"}


@app.post("/predict")
def predict(patient: PatientData):

    # Get model prediction and probability
    probability, prediction = predict_heart_disease(patient)

    # Prediction message
    if prediction == 1:
        prediction_message = (
            "Potential signs of heart disease detected."
        )

    else:
        prediction_message = (
            "No significant signs of heart disease detected."
        )

    # Get risk level
    risk_level = get_risk_level(probability)

    # Get recommendations
    recommendations = get_recommendations(risk_level)

    # Get patient specific advice
    patient_specific_advice = get_patient_specific_advice(
        patient,
        probability
    )

    # Return API response
    return {

        "probability": round(probability, 2),

        "risk_level": risk_level,

        "prediction": prediction_message,

        "medical_advice":
        recommendations["medical_advice"],

        "foods_to_consume":
        recommendations["foods_to_consume"],

        "foods_to_avoid":
        recommendations["foods_to_avoid"],

        "exercise_recommendations":
        recommendations["exercise_recommendations"],

        "patient_specific_advice":
        patient_specific_advice

    }