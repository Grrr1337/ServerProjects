from flask import Flask, request, jsonify

app = Flask(__name__)

# python -m venv .venv
# .venv\Scripts\Activate
# pip install -r requirements.txt
# python server.py
# python client.py 

@app.route("/")
def read_root():
    return jsonify({"Hello": "World"})

@app.route("/add")
def add():
    x = float(request.args.get("x"))
    y = float(request.args.get("y"))
    return jsonify({"result": x + y})

@app.route("/subtract")
def subtract():
    x = float(request.args.get("x"))
    y = float(request.args.get("y"))
    return jsonify({"result": x - y})

@app.route("/multiply")
def multiply():
    x = float(request.args.get("x"))
    y = float(request.args.get("y"))
    return jsonify({"result": x * y})

@app.route("/divide")
def divide():
    x = float(request.args.get("x"))
    y = float(request.args.get("y"))
    if y != 0:
        return jsonify({"result": x / y})
    else:
        return jsonify({"error": "Cannot divide by zero (flask server)"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
