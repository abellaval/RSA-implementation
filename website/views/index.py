from website.app import app
from flask import render_template
from website.models.election import Election


@app.route("/")
def index():
    election_query = [(election.id, election.name, election.description)
                      for election in Election.query.all()]
    return render_template("index.html")
