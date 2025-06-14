from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["operator"]

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    error = "0 で割ることはできません。"
                else:
                    result = num1 / num2
            else:
                error = "無効な演算子です。"

        except ValueError:
            error = "数値を正しく入力してください。"

    return render_template("WebApp.html", result=result, error=error)
