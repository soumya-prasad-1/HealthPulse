import os
import pandas as pd


# Find the project folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# WHO risk CSV file
WHO_RISK_FILE = os.path.join(
    BASE_DIR,
    "data",
    "who_south_asia_risk.csv"
)

# Load WHO risk data
who_risk_data = pd.read_csv(WHO_RISK_FILE)


def get_age_group(age):

    if 40 <= age <= 44:
        return "40-44"
    elif 45 <= age <= 49:
        return "45-49"
    elif 50 <= age <= 54:
        return "50-54"
    elif 55 <= age <= 59:
        return "55-59"
    elif 60 <= age <= 64:
        return "60-64"
    elif 65 <= age <= 69:
        return "65-69"
    elif 70 <= age <= 74:
        return "70-74"

    raise ValueError(
        "WHO risk assessment is available for ages 40 to 74."
    )


def get_sbp_group(sbp):

    if sbp < 120:
        return "<120"
    elif sbp < 140:
        return "120-139"
    elif sbp < 160:
        return "140-159"
    elif sbp < 180:
        return "160-179"
    else:
        return "≥180"


def get_cholesterol_group(cholesterol):

    if cholesterol < 4:
        return "<4"
    elif cholesterol < 5:
        return "4-4.9"
    elif cholesterol < 6:
        return "5-5.9"
    elif cholesterol < 7:
        return "6-6.9"
    else:
        return ">=7"


def get_risk_category(risk):

    if risk < 5:
        return "Very Low Risk"
    elif risk < 10:
        return "Low Risk"
    elif risk < 20:
        return "Moderate Risk"
    elif risk < 30:
        return "High Risk"
    else:
        return "Very High Risk"


def calculate_who_risk(
    age,
    sex,
    smoking,
    systolic_bp,
    total_cholesterol,
    diabetes
):

    # Convert age into WHO age group
    age_group = get_age_group(age)

    # Validate sex
    sex = sex.lower()

    if sex not in ["male", "female"]:
        raise ValueError("Sex must be Male or Female.")

    sex = sex.capitalize()

    # Convert values into WHO categories
    sbp_group = get_sbp_group(systolic_bp)

    cholesterol_group = get_cholesterol_group(
        total_cholesterol
    )

    smoking_group = "Smoker" if smoking else "Non-smoker"

    diabetes_group = "Yes" if diabetes else "No"

    # Find matching row in WHO CSV
    match = who_risk_data[
        (who_risk_data["age_group"] == age_group) &
        (who_risk_data["sex"] == sex) &
        (who_risk_data["smoking"] == smoking_group) &
        (who_risk_data["diabetes"] == diabetes_group) &
        (who_risk_data["sbp_group"] == sbp_group) &
        (who_risk_data["cholesterol_group"] == cholesterol_group)
    ]

    # If no matching row is found
    if match.empty:
        raise ValueError(
            "Risk value could not be found for the supplied combination."
        )

    # Get risk percentage
    risk = float(
        match.iloc[0]["risk_percentage"]
    )

    return {
        "risk_percentage": risk,
        "risk_category": get_risk_category(risk),
        "age_group": age_group,
        "systolic_bp_group": sbp_group,
        "cholesterol_group": cholesterol_group,
        "smoking_status": smoking_group,
        "diabetes_status": diabetes_group
    }