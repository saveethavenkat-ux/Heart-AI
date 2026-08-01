import streamlit as st
import requests
from pdf_report import create_health_report


st.set_page_config(
    page_title="Heart AI",
    page_icon="❤️",
    layout="centered"
)


st.sidebar.title("❤️ Heart AI")

st.sidebar.info(
    """
Heart Disease Prediction Assistant

Built using:

- Machine Learning
- Logistic Regression
- FastAPI
- Streamlit

This application predicts heart disease risk and provides lifestyle recommendations.
"""
)


st.title("❤️ Heart AI")

st.subheader(
    "An Intelligent Heart Disease Prediction Assistant"
)

st.markdown("---")

st.header("Patient Details")

st.info(
    """
Please enter the patient's medical information below.
All fields are required for accurate heart disease prediction.
"""
)


col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120
    )

with col2:
    sex = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

col1, col2 = st.columns(2)

with col1:
    cp = st.number_input(
        "Chest Pain Type",
        min_value=0,
        max_value=3,
        help="""
0 = Typical Angina

1 = Atypical Angina

2 = Non-anginal Pain

3 = Asymptomatic
"""
    )

with col2:
    trestbps = st.number_input(
        "Resting Blood Pressure",
        min_value=50,
        max_value=250
    )

col1, col2 = st.columns(2)

with col1:
    chol = st.number_input(
        "Cholesterol",
        min_value=50,
        max_value=700
    )

with col2:
    fbs = st.selectbox(
        "Fasting Blood Sugar",
        [0, 1],
        help="""
0 = <=120 mg/dl

1 = >120 mg/dl
"""
    )

col1, col2 = st.columns(2)

with col1:
    restecg = st.number_input(
        "Rest ECG",
        min_value=0,
        max_value=2
    )

with col2:
    thalach = st.number_input(
        "Maximum Heart Rate",
        min_value=50,
        max_value=250
    )

col1, col2 = st.columns(2)

with col1:
    exang = st.selectbox(
        "Exercise Induced Angina",
        [0, 1]
    )

with col2:
    oldpeak = st.number_input(
        "Old Peak",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

col1, col2 = st.columns(2)

with col1:
    slope = st.number_input(
        "Slope",
        min_value=0,
        max_value=2
    )

with col2:
    ca = st.number_input(
        "CA",
        min_value=0,
        max_value=4
    )

thal = st.number_input(
    "Thal",
    min_value=0,
    max_value=3
)

st.markdown("---")

predict_button = st.button("Predict Heart Risk")



if predict_button:
    with st.spinner(
    "Generating your Heart AI Health Report..."
):
        patient_data = {
        "age": age,
        "sex": 1 if sex == "Male" else 0,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }

    try:

        response = requests.post(
            "https://https://heart-ai-api-o0i6.onrender.com/predict",
            json=patient_data
        )

        result = response.json()

        st.markdown("---")

        probability_percentage = (
            result["probability"] * 100
        )
        health_score = 100 - probability_percentage

        st.subheader("Heart Disease Probability")

        st.write(
            f"{probability_percentage:.1f}%"
        )
        st.subheader("Heart Health Score")
        st.write(
    f"{health_score:.1f} / 100"
)
        st.progress(
    float(health_score / 100)
)

        st.progress(
            float(result["probability"])
        )

        if result["risk_level"] == "LOW":
            st.success("LOW RISK")

        elif result["risk_level"] == "MODERATE":
            st.warning("MODERATE RISK")

        else:
            st.error("HIGH RISK")

        st.subheader("Prediction")
        st.write(result["prediction"])

        st.subheader("Medical Advice")
        st.write(result["medical_advice"])

        st.subheader("Foods To Consume")

        for food in result["foods_to_consume"]:
            st.write(f"✅ {food}")

        st.subheader("Foods To Avoid")
        st.subheader("Recommended Exercises")
        for exercise in result["exercise_recommendations"]:
          st.write(f"🏃 {exercise}")

        for food in result["foods_to_avoid"]:
            st.write(f"❌ {food}")

        if "patient_specific_advice" in result:

            st.subheader("Patient Specific Advice")

            for advice in result["patient_specific_advice"]:
                st.write(f"• {advice}")

        if result["risk_level"] == "HIGH":

            st.error(
                """
EMERGENCY WARNING

Please consult a cardiologist immediately.

Seek medical attention if you experience:

• Chest pain
• Severe fatigue
• Shortness of breath
• Dizziness
"""
            )

        pdf_file = create_health_report(result)

        st.download_button(
            label="Download Health Report (PDF)",
            data=pdf_file,
            file_name="HeartAI_Report.pdf",
            mime="application/pdf"
        )

    except Exception:

        st.error(
            """
Unable to connect to the FastAPI server.

Please make sure that:

1. FastAPI is running.
2. Uvicorn is running on port 8000.
3. The backend has no errors.
"""
        )


st.markdown("---")

st.warning(
    """
DISCLAIMER

This application is intended for educational purposes only.

It should not be used as a substitute for professional medical advice, diagnosis, or treatment.

Please consult a qualified healthcare professional for any medical concerns.
"""
)