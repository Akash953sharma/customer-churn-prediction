import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("customer_churn.csv")

# Convert columns
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.fillna(0, inplace=True)

# Target
df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

# Only 4 features
X = df[[
    "SeniorCitizen",
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]]

y = df["Churn"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print("Accuracy:", accuracy)

# Save model
joblib.dump(model, "churn_model.pkl")
print("Model Saved Successfully!")
