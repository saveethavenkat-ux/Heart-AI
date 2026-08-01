THRESHOLD = 0.35

MODEL_PATH = "models/heart_model.pkl"
SCALER_PATH = "models/scaler.pkl"


RISK_LEVELS = {
    "low": (0.0, 0.35),
    "moderate": (0.35, 0.70),
    "high": (0.70, 1.00)
}