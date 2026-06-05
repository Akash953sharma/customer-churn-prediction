import joblib
import pandas as pd

# Load model
model = joblib.load("churn_model.pkl")

print("Model Loaded Successfully!")

# Sample customer data
data = {
    "SeniorCitizen": [0],
    "tenure": [24],
    "MonthlyCharges": [70],
    "TotalCharges": [1680],

    "gender_Male": [1],
    "Partner_Yes": [1],
    "Dependents_Yes": [0],
    "PhoneService_Yes": [1],
    "MultipleLines_No phone service": [0],
    "MultipleLines_Yes": [1],
    "InternetService_Fiber optic": [1],
    "InternetService_No": [0],
    "OnlineSecurity_No internet service": [0],
    "OnlineSecurity_Yes": [1],
    "OnlineBackup_No internet service": [0],
    "OnlineBackup_Yes": [1],
    "DeviceProtection_No internet service": [0],
    "DeviceProtection_Yes": [1],
    "TechSupport_No internet service": [0],
    "TechSupport_Yes": [1],
    "StreamingTV_No internet service": [0],
    "StreamingTV_Yes": [1],
    "StreamingMovies_No internet service": [0],
    "StreamingMovies_Yes": [1],
    "Contract_One year": [1],
    "Contract_Two year": [0],
    "PaperlessBilling_Yes": [1],
    "PaymentMethod_Credit card (automatic)": [1],
    "PaymentMethod_Electronic check": [0],
    "PaymentMethod_Mailed check": [0]
}

df = pd.DataFrame(data)

prediction = model.predict(df)

if prediction[0] == 1:
    print("⚠️ Customer May Churn")
else:
    print("✅ Customer Will Stay")
