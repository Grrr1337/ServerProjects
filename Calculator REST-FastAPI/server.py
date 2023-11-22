from fastapi import FastAPI
from uvicorn import run

# .venv\Scripts\Activate
# pip install -r requirements.txt
# python server.py

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add")
def add(x: float, y: float):
    return {"result": x + y}

@app.get("/subtract")
def subtract(x: float, y: float):
    return {"result": x - y}

@app.get("/multiply")
def multiply(x: float, y: float):
    return {"result": x * y}

@app.get("/divide")
def divide(x: float, y: float):
    if y != 0:
        return {"result": x / y}
    else:
        return {"error": "Cannot divide by zero"}


if __name__ == "__main__":
    run(app, host="127.0.0.1", port=8000)
