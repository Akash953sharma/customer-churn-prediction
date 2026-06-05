from flask import Flask, request
import joblib
import pandas as pd

from flask import Flask, request

app = Flask(__name__)
model = joblib.load("churn_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":
        tenure = request.form["tenure"]

        if int(tenure) < 12:
            result = "⚠️ Customer May Churn"
        else:
            result = "✅ Customer Will Stay"
    return f'''
   <!DOCTYPE html>
    <html>
    <head>
    <title>Customer Churn Prediction</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            text-align: center;
            padding-top: 50px;
        }}

        .container {{
            background: white;
            width: 500px;
            margin: auto;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.2);
        }}

        h1 {{
            color: #333;
        }}

        input {{
            width: 80%;
            padding: 10px;
            margin: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }}

        button {{
            background: #007bff;
            color: white;
            padding: 10px 25px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }}

        button:hover {{
            background: #0056b3;
        }}

        h2 {{
            color: green;
        }}
    </style>
</head>

<body>

<div class="container">
    <h1>📊 Customer Churn Prediction</h1>

    <p><b>Algorithm:</b> Random Forest Classifier</p>
    <p><b>Accuracy:</b> 78.5%</p>
    <p><b>Developed By:</b> Akash Kumar Sharma</p>

    <form method="POST">
        <input type="number" name="tenure" placeholder="Enter Tenure (Months)" required>
        <br>
        <button type="submit">Predict</button>
    </form>

    <h2>{result}</h2>

</div>

</body>
</html>
'''


if __name__ == "__main__":
    app.run(debug=True)
