from flask import Flask, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("churn_model.pkl")


# HOME PAGE
@app.route("/")
def home():

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Customer Churn Prediction</title>

        <style>

        body{
            font-family:Segoe UI;
            background:linear-gradient(135deg,#667eea,#764ba2);
            color:white;
            text-align:center;
            padding:50px;
        }

        .container{
            max-width:800px;
            margin:auto;
            background:rgba(255,255,255,0.15);
            padding:40px;
            border-radius:20px;
            backdrop-filter:blur(10px);
        }

        h1{
            font-size:42px;
        }

        p{
            font-size:18px;
            line-height:1.8;
        }

        button{
            background:#00c853;
            color:white;
            border:none;
            padding:15px 30px;
            border-radius:10px;
            font-size:18px;
            cursor:pointer;
        }

        button:hover{
            background:#00a844;
        }

        </style>

    </head>

    <body>

    <div class="container">

        <h1>📊 Customer Churn Prediction</h1>

        <p>
        Customer Churn Prediction is a Machine Learning project
        that predicts whether a customer is likely to leave
        a company's service or continue using it.
        </p>

        <p>
        This project uses a Random Forest Classifier and
        customer data such as tenure, monthly charges and
        total charges to predict churn behaviour.
        </p>

        <h3>Algorithm : Random Forest</h3>
        <h3>Accuracy : 78.5%</h3>
        <h3>Developer : Akash Kumar Sharma</h3>

        <br>

        <a href="/predict">
            <button>Start Prediction 🚀</button>
        </a>

    </div>

    </body>
    </html>
    """


# PREDICTION PAGE
@app.route("/predict", methods=["GET", "POST"])
def predict():

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

        try:

            prediction = model.predict(data)

            if prediction[0] == 1:
                result = "⚠️ Customer May Churn"
            else:
                result = "✅ Customer Will Stay"

        except:
            result = "Prediction Error"

    return f"""
    <!DOCTYPE html>

    <html>
    <head>

    <title>Prediction</title>

    <style>

    body{{
        font-family:Segoe UI;
        background:linear-gradient(135deg,#667eea,#764ba2);
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
    }}

    .container{{
        width:500px;
        background:white;
        padding:40px;
        border-radius:20px;
        text-align:center;
        box-shadow:0 10px 30px rgba(0,0,0,0.3);
    }}

    input{{
        width:90%;
        padding:12px;
        margin:10px;
        border-radius:8px;
        border:1px solid #ccc;
    }}

    button{{
        background:#4f46e5;
        color:white;
        border:none;
        padding:12px 25px;
        border-radius:8px;
        cursor:pointer;
    }}

    .result{{
        margin-top:20px;
        font-size:24px;
        font-weight:bold;
    }}

    a{{
        text-decoration:none;
    }}

    </style>

    </head>

    <body>

    <div class="container">

        <h1>Prediction Page</h1>

        <form method="POST">

        <input type="number"
        name="SeniorCitizen"
        placeholder="Senior Citizen (0/1)"
        required>

        <input type="number"
        name="tenure"
        placeholder="Tenure (Months)"
        required>

        <input type="number"
        step="0.01"
        name="MonthlyCharges"
        placeholder="Monthly Charges"
        required>

        <input type="number"
        step="0.01"
        name="TotalCharges"
        placeholder="Total Charges"
        required>

        <br>

        <button type="submit">
        Predict
        </button>

        </form>

        <div class="result">
        {result}
        </div>

        <br>

        <a href="/">
            ← Back To Home
        </a>

    </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
