import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


# ==============================
# 1. LOAD DATASET
# ==============================

df = pd.read_csv("data/cardio_cleaned.csv")

print("Dataset shape:", df.shape)


# ==============================
# 2. REMOVE ID
# ==============================

df = df.drop(columns=["id"])


# ==============================
# 3. FEATURES AND TARGET
# ==============================

X = df.drop(columns=["cardio"])
y = df["cardio"]


# ==============================
# 4. TRAIN-TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==============================
# 5. DEFINE MODELS
# ==============================

models = {

    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ]),

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    ),

    "KNN": Pipeline([
        ("scaler", StandardScaler()),
        ("model", KNeighborsClassifier(n_neighbors=5))
    ]),

    "SVM": Pipeline([
        ("scaler", StandardScaler()),
        ("model", SVC(
            kernel="rbf",
            probability=False,
            random_state=42
        ))
    ])
}


# ==============================
# 6. TRAIN AND EVALUATE
# ==============================

results = []

for name, model in models.items():

    print("\nTraining:", name)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # ROC-AUC score
    if hasattr(model, "decision_function"):
        y_score = model.decision_function(X_test)
    else:
        y_score = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_score)

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "ROC-AUC": roc_auc
    })

    print("Accuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))
    print("F1 Score :", round(f1, 4))
    print("ROC-AUC  :", round(roc_auc, 4))


# ==============================
# 7. RESULTS TABLE
# ==============================

results_df = pd.DataFrame(results)

print("\n====================================")
print("MODEL COMPARISON")
print("====================================")

print(results_df.to_string(index=False))


# ==============================
# 8. SELECT BEST MODEL
# ==============================

best_index = results_df["F1 Score"].idxmax()

best_model_name = results_df.loc[best_index, "Model"]

best_model = models[best_model_name]


print("\n====================================")
print("BEST MODEL")
print("====================================")

print("Model:", best_model_name)


# ==============================
# 9. SAVE BEST MODEL
# ==============================

joblib.dump(
    best_model,
    "ml/healthpulse_model.pkl"
)

print("\nModel saved successfully:")
print("ml/healthpulse_model.pkl")