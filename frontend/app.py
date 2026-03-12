from flask import Flask
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend-service:5000"

@app.route("/")
def home():
    return "Frontend Service Running"

@app.route("/backend")
def backend():
    response = requests.get(f"{BACKEND_URL}/api")
    return response.json()

@app.route("/health")
def health():
    return {"status": "frontend healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)