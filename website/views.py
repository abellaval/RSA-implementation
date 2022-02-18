from flask import render_template, request, make_response
from database import get_db


def index():
    # db = get_db()
    # print(db.execute("SELECT * FROM election").fetchall())
    return render_template("index.html", elections_info=[
        (1, "name1", "desc1"),
        (2, "name2", "desc2"),
        (3, "name3", "desc3")
    ])


def election(id):
    return render_template("election.html", id=id)
