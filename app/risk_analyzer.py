from config import RISK_LEVELS


def get_risk_level(probability):

    if RISK_LEVELS["low"][0] <= probability < RISK_LEVELS["low"][1]:
        return "LOW"

    elif RISK_LEVELS["moderate"][0] <= probability < RISK_LEVELS["moderate"][1]:
        return "MODERATE"

    else:
        return "HIGH"