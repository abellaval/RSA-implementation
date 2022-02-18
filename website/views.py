from flask import render_template
from database import get_db


def index():
    # db = get_db()
    # print(db.execute("SELECT * FROM election").fetchall())
    return render_template("index.html")