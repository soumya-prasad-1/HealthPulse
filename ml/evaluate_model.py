import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)


# ==============================
# 1. LOAD DATASET
# ==============================

df = pd.read_csv("data/cardio_cleaned.csv")

df = df.drop(columns=["id"])

X = df.drop(columns=["cardio"])
y = df["cardio"]


# ==============================
# 2. SAME TRAIN-TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==============================
# 3. LOAD SAVED MODEL
# ==============================

model = joblib.load("ml/healthpulse_model.pkl")

print("Saved model loaded successfully.")


# ==============================
# 4. MAKE PREDICTIONS
# ==============================

y_pred = model.predict(X_test)

y_score = model.decision_function(X_test)


# ==============================
# 5. METRICS
# ==============================

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_score)


print("\n====================================")
print("FINAL MODEL EVALUATION")
print("====================================")

print("Accuracy :", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall   :", round(recall, 4))
print("F1 Score :", round(f1, 4))
print("ROC-AUC  :", round(roc_auc, 4))


# ==============================
# 6. CONFUSION MATRIX
# ==============================

cm = confusion_matrix(y_test, y_pred)

print("\n====================================")
print("CONFUSION MATRIX")
print("====================================")

print(cm)


# ==============================
# 7. CLASSIFICATION REPORT
# ==============================

print("\n====================================")
print("CLASSIFICATION REPORT")
print("====================================")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "No Cardiovascular Disease",
            "Cardiovascular Disease"
        ]
    )
)


# ==============================
# 8. CONFUSION MATRIX VALUES
# ==============================

tn, fp, fn, tp = cm.ravel()

print("\n====================================")
print("CONFUSION MATRIX DETAILS")
print("====================================")

print("True Negatives :", tn)
print("False Positives:", fp)
print("False Negatives:", fn)
print("True Positives :", tp)

print("\nEvaluation complete.")