from flask import Flask, render_template
import config

app = Flask(__name__)

if app.config.get("DEBUG"):
    app.config.from_object(config.Debug())
else:
    app.config.from_object(config.Production())


@app.route("/")
def home():
    return render_template("home.html")
