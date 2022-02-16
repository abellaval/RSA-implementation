from flask import render_template
from website.client import app


@app.route("/")
def index():
    return render_template("index.html")
