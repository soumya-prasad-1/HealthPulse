import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 1. LOAD CLEANED DATASET
# ==============================

df = pd.read_csv("data/cardio_cleaned.csv")

print("Dataset shape:", df.shape)

# ==============================
# 2. TARGET DISTRIBUTION
# ==============================

plt.figure(figsize=(7, 5))

sns.countplot(data=df, x="cardio")

plt.title("Cardiovascular Disease Distribution")
plt.xlabel("Cardiovascular Disease")
plt.ylabel("Number of Patients")

plt.xticks([0, 1], ["No Disease", "Disease"])

plt.show()


# ==============================
# 3. AGE DISTRIBUTION
# ==============================

plt.figure(figsize=(8, 5))

sns.histplot(data=df, x="age", bins=30, kde=True)

plt.title("Age Distribution")
plt.xlabel("Age (Years)")
plt.ylabel("Number of Patients")

plt.show()


# ==============================
# 4. AGE VS CARDIO
# ==============================

plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x="cardio", y="age")

plt.title("Age vs Cardiovascular Disease")
plt.xlabel("Cardiovascular Disease")
plt.ylabel("Age (Years)")

plt.xticks([0, 1], ["No Disease", "Disease"])

plt.show()


# ==============================
# 5. BMI VS CARDIO
# ==============================

plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x="cardio", y="bmi")

plt.title("BMI vs Cardiovascular Disease")
plt.xlabel("Cardiovascular Disease")
plt.ylabel("BMI")

plt.xticks([0, 1], ["No Disease", "Disease"])

plt.show()


# ==============================
# 6. BLOOD PRESSURE VS CARDIO
# ==============================

plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x="cardio", y="ap_hi")

plt.title("Systolic Blood Pressure vs Cardiovascular Disease")
plt.xlabel("Cardiovascular Disease")
plt.ylabel("Systolic Blood Pressure")

plt.xticks([0, 1], ["No Disease", "Disease"])

plt.show()


# ==============================
# 7. CHOLESTEROL VS CARDIO
# ==============================

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="cholesterol", hue="cardio")

plt.title("Cholesterol Level vs Cardiovascular Disease")
plt.xlabel("Cholesterol Category")
plt.ylabel("Number of Patients")

plt.show()


# ==============================
# 8. GLUCOSE VS CARDIO
# ==============================

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="gluc", hue="cardio")

plt.title("Glucose Level vs Cardiovascular Disease")
plt.xlabel("Glucose Category")
plt.ylabel("Number of Patients")

plt.show()


# ==============================
# 9. SMOKING VS CARDIO
# ==============================

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="smoke", hue="cardio")

plt.title("Smoking vs Cardiovascular Disease")
plt.xlabel("Smoking")
plt.ylabel("Number of Patients")

plt.show()


# ==============================
# 10. PHYSICAL ACTIVITY VS CARDIO
# ==============================

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="active", hue="cardio")

plt.title("Physical Activity vs Cardiovascular Disease")
plt.xlabel("Physical Activity")
plt.ylabel("Number of Patients")

plt.show()


print("\n===== EDA COMPLETE =====")