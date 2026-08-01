def get_recommendations(risk_level):

    recommendations = {

        "LOW": {

            "medical_advice":
            "Maintain a healthy lifestyle. Exercise regularly and undergo routine health checkups.",

            "foods_to_consume": [
                "Fruits",
                "Vegetables",
                "Whole grains",
                "Oats",
                "Low-fat milk",
                "Nuts"
            ],

            "foods_to_avoid": [
                "Processed foods",
                "Sugary drinks",
                "Excess salt",
                "Fast food"
            ],

            "exercise_recommendations": [
                "30 minutes of brisk walking",
                "Cycling",
                "Swimming",
                "Light jogging",
                "Stretching exercises"
            ]

        },

        "MODERATE": {

            "medical_advice":
            "Monitor your heart health regularly. Consult a doctor if symptoms persist and maintain a heart-healthy diet.",

            "foods_to_consume": [
                "Leafy green vegetables",
                "Fish",
                "Olive oil",
                "Brown rice",
                "Almonds",
                "Beans"
            ],

            "foods_to_avoid": [
                "High sodium foods",
                "Deep fried foods",
                "Processed meat",
                "Excess sugar"
            ],

            "exercise_recommendations": [
                "Brisk walking",
                "Yoga",
                "Meditation",
                "Stretching",
                "Low intensity cardio"
            ]

        },

        "HIGH": {

            "medical_advice":
            "High risk of heart disease detected. Please consult a cardiologist immediately and follow medical advice.",

            "foods_to_consume": [
                "Oats",
                "Salmon",
                "Avocados",
                "Spinach",
                "Walnuts",
                "Low-fat dairy products"
            ],

            "foods_to_avoid": [
                "Fried foods",
                "High cholesterol foods",
                "Sugary drinks",
                "Red meat",
                "Fast food",
                "High sodium foods"
            ],

            "exercise_recommendations": [
                "Doctor supervised exercise",
                "Light walking",
                "Breathing exercises",
                "Meditation",
                "Avoid strenuous workouts"
            ]

        }

    }

    return recommendations[risk_level]


def get_cholesterol_advice(chol):

    advice = []

    if chol < 200:
        advice.append(
            "Your cholesterol level is within the healthy range."
        )

    elif 200 <= chol < 240:
        advice.append(
            "Your cholesterol level is slightly elevated. Reduce oily and processed foods."
        )

    else:
        advice.append(
            "Your cholesterol level is high. Avoid fried foods and consume more fibre-rich foods such as oats and fruits."
        )

    return advice


def get_bp_advice(trestbps):

    advice = []

    if trestbps < 120:
        advice.append(
            "Your blood pressure is normal."
        )

    elif 120 <= trestbps < 140:
        advice.append(
            "Your blood pressure is slightly elevated. Reduce salt intake and exercise regularly."
        )

    else:
        advice.append(
            "Your blood pressure is high. Regular monitoring and medical consultation are recommended."
        )

    return advice


def get_diabetes_advice(fbs):

    advice = []

    if fbs == 1:
        advice.append(
            "Your fasting blood sugar level may be elevated. Limit sugary foods and monitor glucose levels regularly."
        )

    else:
        advice.append(
            "Your fasting blood sugar level appears normal."
        )

    return advice


def get_age_advice(age):

    advice = []

    if age >= 60:

        advice.append(
            "Regular cardiovascular health checkups are recommended for individuals aged 60 years and above."
        )

        advice.append(
            "Aim for at least 30 minutes of light physical activity every day."
        )

        advice.append(
            "Maintain a heart-healthy diet and monitor blood pressure and cholesterol levels regularly."
        )

    return advice


def get_probability_advice(probability):

    advice = []

    if probability >= 0.70:

        advice.append(
            "Your predicted heart disease risk is high. Immediate medical consultation is strongly recommended."
        )

        advice.append(
            "Seek immediate medical attention if you experience chest pain, shortness of breath, severe fatigue, dizziness or irregular heartbeat."
        )

    elif probability >= 0.40:

        advice.append(
            "Your predicted heart disease risk is moderate. Lifestyle modifications and regular health monitoring are recommended."
        )

    else:

        advice.append(
            "Your predicted heart disease risk is low. Continue maintaining a healthy lifestyle and undergo regular health checkups."
        )

    return advice

def get_patient_specific_advice(patient, probability):

    advice = []

    advice.extend(
        get_cholesterol_advice(patient.chol)
    )

    advice.extend(
        get_bp_advice(patient.trestbps)
    )

    advice.extend(
        get_diabetes_advice(patient.fbs)
    )

    advice.extend(
        get_age_advice(patient.age)
    )

    advice.extend(
        get_probability_advice(probability)
    )

    return advice