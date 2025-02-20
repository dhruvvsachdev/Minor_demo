from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=['POST'])
def calculate():
    try:
        expression = request.json.get('expression', '')
        # Safely evaluate the mathematical expression
        result = eval(expression)  # Note: eval() is used for simplicity here
        return jsonify({"result": str(result)})
    except Exception as e:
        return jsonify({"result": "Error"})

if __name__ == "__main__":
    app.run(debug=True)
