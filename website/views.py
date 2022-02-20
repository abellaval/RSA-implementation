from flask import render_template, request, make_response
from database import get_db
import models.dummy_data as dummy_data


def index():
    elections_info = [
        (dummy_data.election_1.id, dummy_data.election_1.name,
         dummy_data.election_1.description),
        (dummy_data.election_2.id, dummy_data.election_2.name,
         dummy_data.election_2.description),
        (dummy_data.election_3.id, dummy_data.election_3.name,
         dummy_data.election_3.description),
    ]
    return render_template("index.html", elections_info=elections_info)


def election(election_id):
    election = next(filter(lambda election:
                           election.id == election_id,
                           dummy_data.all_elections),
                    None)
    return render_template("election.html", election=election)


def result(election_id):
    # TODO: check if we have already voted
    election = next(filter(lambda election:
                           election.id == election_id,
                           dummy_data.all_elections),
                    None)
    return render_template("result.html", election=election)
