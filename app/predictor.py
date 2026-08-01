import joblib

from config import MODEL_PATH
from config import SCALER_PATH


model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


import pandas as pd

from config import THRESHOLD


def predict_heart_disease(patient):

    data = pd.DataFrame({
        "age": [patient.age],
        "sex": [patient.sex],
        "cp": [patient.cp],
        "trestbps": [patient.trestbps],
        "chol": [patient.chol],
        "fbs": [patient.fbs],
        "restecg": [patient.restecg],
        "thalach": [patient.thalach],
        "exang": [patient.exang],
        "oldpeak": [patient.oldpeak],
        "slope": [patient.slope],
        "ca": [patient.ca],
        "thal": [patient.thal]
    })

    scaled_data = scaler.transform(data)

    probability = model.predict_proba(scaled_data)[0][1]

    prediction = int(probability >= THRESHOLD)

    return probability, prediction

