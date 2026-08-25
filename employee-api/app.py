from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": os.getenv("APP_NAME", "Employee API")
    }

@app.route("/health")
def health():
    return {
        "status": "UP"
    }

@app.route("/version")
def version():
    return {
        "version": os.getenv("APP_VERSION", "1.0")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
