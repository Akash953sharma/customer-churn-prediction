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

        input_data = pd.DataFrame({
            "SeniorCitizen": [senior],
            "tenure": [tenure],
            "MonthlyCharges": [monthly],
            "TotalCharges": [total]
        })

        try:
            prediction = model.predict(input_data)

            if prediction[0] == 1:
                result = "⚠️ Customer May Churn"
            else:
                result = "✅ Customer Will Stay"

        except:
            result = "Prediction Error"

    return f'''
<!DOCTYPE html>
<html>
<head>
<title>Customer Churn Prediction</title>

<style>

*{{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Segoe UI',sans-serif;
}}

body{{
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:linear-gradient(135deg,#667eea,#764ba2);
}}

.container{{
width:500px;
background:rgba(255,255,255,0.15);
backdrop-filter:blur(15px);
padding:40px;
border-radius:20px;
box-shadow:0 8px 32px rgba(0,0,0,0.3);
text-align:center;
color:white;
}}

h1{{
margin-bottom:10px;
font-size:36px;
}}

.subtitle{{
margin-bottom:20px;
opacity:0.9;
}}

.info{{
margin-bottom:25px;
line-height:1.8;
}}

input{{
width:100%;
padding:12px;
margin:10px 0;
border:none;
border-radius:10px;
font-size:16px;
}}

button{{
background:#00c853;
color:white;
border:none;
padding:12px 30px;
border-radius:10px;
font-size:18px;
cursor:pointer;
margin-top:10px;
transition:0.3s;
}}

button:hover{{
background:#00a844;
transform:scale(1.05);
}}

.result{{
margin-top:25px;
font-size:24px;
font-weight:bold;
}}

.footer{{
margin-top:25px;
font-size:12px;
opacity:0.8;
}}

</style>
</head>

<body>

<div class="container">

<h1>📊 Customer Churn Prediction</h1>

<p class="subtitle">
Machine Learning Based Prediction System
</p>

<div class="info">
<b>Algorithm:</b> Random Forest<br>
<b>Accuracy:</b> 78.5%<br>
<b>Developed By:</b> Akash Kumar Sharma
</div>

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

<button type="submit">
Predict
</button>

</form>

<div class="result">
{result}
</div>

<div class="footer">
© 2026 Customer Churn Prediction Project
</div>

</div>

</body>
</html>
'''


if __name__ == "__main__":
    app.run(debug=True)
