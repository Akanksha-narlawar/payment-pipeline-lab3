from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application": "payment-api",
        "version": os.getenv("APP_VERSION", "unknown"),
        "git_commit": os.getenv("GIT_COMMIT", "unknown"),
        "jenkins_build": os.getenv("BUILD_NUMBER", "unknown")
    }

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)