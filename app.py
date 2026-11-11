import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", message="Hello from the Cloud!")

if __name__ == "__main__":
    # Use the PORT environment variable provided by the cloud host, defaulting to 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
