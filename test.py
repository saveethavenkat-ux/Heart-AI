from app.risk_analyzer import get_risk_level
from app.recommendations import get_recommendations


# Example probability from your model
probability = 0.82

# Get the risk level
risk_level = get_risk_level(probability)

# Get recommendations
recommendation = get_recommendations(risk_level)

print("Risk Level:", risk_level)
print()
print(recommendation)