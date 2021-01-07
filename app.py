import os
from flask import Flask, request


app = Flask(__name__)
app.config.from_object(os.getenv("APP_SETTINGS", "config.DevelopmentConfig"))


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/message", methods=["POST"])
def message():
    data = request.get_json(force=True)
    text = data.get("text")
    return f"You said: {text}"


if __name__ == "__main__":
    PORT = os.getenv("PORT", 5000)
    DEBUG = os.getenv("DEBUG", False)
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)