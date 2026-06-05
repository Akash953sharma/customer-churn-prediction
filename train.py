import joblib
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Dataset load
df = pd.read_csv("customer_churn.csv")

# Customer ID remove
df.drop("customerID", axis=1, inplace=True)

# TotalCharges ko number me convert karo
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Missing values fill karo
df.fillna(0, inplace=True)

# Churn column ko convert karo
df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

# Text columns ko numeric me convert karo
df = pd.get_dummies(df, drop_first=True)

print(df.columns)
print(df.head())
print(df.shape)


# Features and Target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = RandomForestClassifier(random_state=42)

# Train Model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)


# Model Save
joblib.dump(model, "churn_model.pkl")

print("Model Saved Successfully!")
