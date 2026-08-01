from io import BytesIO
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable
)

from reportlab.lib.styles import getSampleStyleSheet


def create_health_report(result):

    # Create an in-memory PDF file
    buffer = BytesIO()

    pdf = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    # ------------------------------------------------
    # TITLE
    # ------------------------------------------------

    elements.append(
        Paragraph(
            "HEART AI",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "Comprehensive Cardiovascular Health Report",
            styles["Heading2"]
        )
    )

    elements.append(Spacer(1, 10))

    # ------------------------------------------------
    # PROBABILITY
    # ------------------------------------------------

    elements.append(
        Paragraph(
            f"Heart Disease Probability : {result['probability'] * 100:.1f} %",
            styles["BodyText"]
        )
    )

    health_score = 100 - (result["probability"] * 100)

    elements.append(
        Paragraph(
            f"Heart Health Score : {health_score:.1f} / 100",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 5))

    # ------------------------------------------------
    # RISK LEVEL
    # ------------------------------------------------

    elements.append(
        Paragraph(
            f"Risk Level : {result['risk_level']}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 5))

    # ------------------------------------------------
    # PREDICTION
    # ------------------------------------------------

    elements.append(
        Paragraph(
            f"Prediction : {result['prediction']}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 10))

    # ------------------------------------------------
    # MEDICAL ADVICE
    # ------------------------------------------------

    elements.append(
        Paragraph(
            "Medical Advice",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            result["medical_advice"],
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 10))

    # ------------------------------------------------
    # FOODS TO CONSUME
    # ------------------------------------------------

    elements.append(
        Paragraph(
            "Foods To Consume",
            styles["Heading2"]
        )
    )

    consume_foods = []

    for food in result["foods_to_consume"]:

        consume_foods.append(
            Paragraph(
                food,
                styles["BodyText"]
            )
        )

    elements.append(
        ListFlowable(
            consume_foods,
            bulletType="1"
        )
    )

    elements.append(Spacer(1, 10))

    # ------------------------------------------------
    # FOODS TO AVOID
    # ------------------------------------------------

    elements.append(
        Paragraph(
            "Foods To Avoid",
            styles["Heading2"]
        )
    )

    avoid_foods = []

    for food in result["foods_to_avoid"]:

        avoid_foods.append(
            Paragraph(
                food,
                styles["BodyText"]
            )
        )

    elements.append(
        ListFlowable(
            avoid_foods,
            bulletType="1"
        )
    )

    elements.append(Spacer(1, 10))

    # ------------------------------------------------
    # EXERCISE RECOMMENDATIONS
    # ------------------------------------------------

    elements.append(
        Paragraph(
            "Recommended Exercises",
            styles["Heading2"]
        )
    )

    exercise_list = []

    for exercise in result["exercise_recommendations"]:

        exercise_list.append(
            Paragraph(
                exercise,
                styles["BodyText"]
            )
        )

    elements.append(
        ListFlowable(
            exercise_list,
            bulletType="1"
        )
    )

    elements.append(Spacer(1, 10))

    # ------------------------------------------------
    # PATIENT SPECIFIC ADVICE
    # ------------------------------------------------

    elements.append(
        Paragraph(
            "Patient Specific Advice",
            styles["Heading2"]
        )
    )

    advice_list = []

    for advice in result["patient_specific_advice"]:

        advice_list.append(
            Paragraph(
                advice,
                styles["BodyText"]
            )
        )

    elements.append(
        ListFlowable(
            advice_list,
            bulletType="1"
        )
    )

    elements.append(Spacer(1, 10))

    # ------------------------------------------------
    # REPORT INFORMATION
    # ------------------------------------------------

    elements.append(
        Paragraph(
            "Report Information",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Generated On : {datetime.now().strftime('%d/%m/%Y')}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            "Prediction Model : Logistic Regression",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            "Application Version : Heart AI v1.0",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 10))

    # ------------------------------------------------
    # DISCLAIMER
    # ------------------------------------------------

    elements.append(
        Paragraph(
            "DISCLAIMER",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            "This report is intended for educational purposes only. "
            "It should not be considered a substitute for professional "
            "medical diagnosis or treatment. Please consult a qualified "
            "healthcare professional for medical concerns.",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    # ------------------------------------------------
    # FOOTER
    # ------------------------------------------------

    elements.append(
        Paragraph(
            "Generated by Heart AI",
            styles["Italic"]
        )
    )

    # ------------------------------------------------
    # BUILD PDF
    # ------------------------------------------------

    pdf.build(elements)

    buffer.seek(0)

    return buffer