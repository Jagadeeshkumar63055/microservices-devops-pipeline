from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend Service Running"

@app.route("/api")
def api():
    return {"message": "Backend API response"}

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/slow")
def slow():
    time.sleep(5)
    return {"message": "slow response"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)