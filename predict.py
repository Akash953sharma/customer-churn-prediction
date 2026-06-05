import joblib

# Load saved model
model = joblib.load("churn_model.pkl")

print("Model Loaded Successfully!")

# Check model type
print("Model Type:", type(model))
