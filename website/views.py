from flask import render_template, request, make_response, redirect, url_for
from database import get_db
import models.dummy_data as dummy_data
from website.admin import Admin


def index():
    # TODO: use data from a database fetch
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
    fingerprint = request.cookies.get("fingerprint", default=None)
    # if the fingerprint is empty, redirect to index
    if fingerprint is None:
        return redirect(url_for("index"), code=303)
    admin = Admin.get_admin()
    vote_token = admin.get_vote_token(election_id, fingerprint)
    if vote_token is None:
        # This client has already voted, redirect to result of election
        return redirect(url_for("result", election_id=election_id), code=303)
    # TODO: fetch data from database
    election = next(filter(lambda election:
                           election.id == election_id,
                           dummy_data.all_elections),
                    None)
    # TODO: set hidden vote token for the election (basically set a hidden
    #  input field in the html)
    return render_template("election.html", election=election)


def result(election_id):
    fingerprint = request.cookies.get("fingerprint", default=None)
    # if the fingerprint is empty, redirect to index
    if fingerprint is None:
        return redirect(url_for("index"), code=303)
    admin = Admin.get_admin()
    vote_token = admin.get_vote_token(election_id, fingerprint)
    if vote_token is not None:
        # This client hasn't voted, redirect to choices for election
        return redirect(url_for("election", election_id=election_id), code=303)
    # TODO: fetch data from database
    election = next(filter(lambda election:
                           election.id == election_id,
                           dummy_data.all_elections),
                    None)
    return render_template("result.html", election=election)
