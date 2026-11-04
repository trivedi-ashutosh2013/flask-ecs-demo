from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", app_name=os.getenv("APP_NAME", "Flask Docker Demo"))

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    # 0.0.0.0 makes the app reachable outside the container.
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
