import pandas as pd
from sklearn.model_selection import train_test_split

# ==============================
# 1. LOAD CLEANED DATASET
# ==============================

df = pd.read_csv("data/cardio_cleaned.csv")

print("Dataset shape:", df.shape)


# ==============================
# 2. REMOVE ID
# ==============================

df = df.drop(columns=["id"])


# ==============================
# 3. SEPARATE FEATURES AND TARGET
# ==============================

X = df.drop(columns=["cardio"])
y = df["cardio"]


print("\nFeatures:")
print(X.columns.tolist())

print("\nTarget:")
print("cardio")


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
# 5. DISPLAY RESULTS
# ==============================

print("\n===== DATA SPLIT COMPLETE =====")

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

print("\nTraining target distribution:")
print(y_train.value_counts())

print("\nTesting target distribution:")
print(y_test.value_counts())