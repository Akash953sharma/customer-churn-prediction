from flask import Flask, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("churn_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        senior = int(request.form["SeniorCitizen"])
        tenure = int(request.form["tenure"])
        monthly = float(request.form["MonthlyCharges"])
        total = float(request.form["TotalCharges"])

        data = pd.DataFrame({
            "SeniorCitizen": [senior],
            "tenure": [tenure],
            "MonthlyCharges": [monthly],
            "TotalCharges": [total]
        })

        prediction = model.predict(data)

        if prediction[0] == 1:
            result = "⚠️ Customer May Churn"
        else:
            result = "✅ Customer Will Stay"

    return f"""
    <html>
    <body style='font-family:Arial;text-align:center;padding:40px;background:#f5f5f5;'>

    <h1>📊 Customer Churn Prediction</h1>
    <p><b>Algorithm:</b> Random Forest</p>

    <form method='POST'>

        <input type='number' name='SeniorCitizen'
        placeholder='Senior Citizen (0/1)' required><br><br>

        <input type='number' name='tenure'
        placeholder='Tenure (Months)' required><br><br>

        <input type='number' step='0.01'
        name='MonthlyCharges'
        placeholder='Monthly Charges' required><br><br>

        <input type='number' step='0.01'
        name='TotalCharges'
        placeholder='Total Charges' required><br><br>

        <button type='submit'>Predict</button>

    </form>

    <h2>{result}</h2>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
