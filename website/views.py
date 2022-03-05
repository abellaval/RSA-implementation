from flask import render_template, request, make_response, redirect, url_for, \
    flash
from database import get_db
from website.admin import Admin


def index():
    admin = Admin.get_admin()
    all_elections = admin.get_all_elections()
    return render_template("index.html", all_elections=all_elections)


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
    election = admin.get_election_by_id(election_id)
    return render_template("election.html", election=election,
                           vote_token=vote_token)


def result(election_id):
    fingerprint = request.cookies.get("fingerprint", default=None)
    # if the fingerprint is empty, redirect to index
    if fingerprint is None:
        return redirect(url_for("index"), code=303)
    admin = Admin.get_admin()
    vote_token = admin.get_vote_token(election_id, fingerprint)
    # FIXME: commented for testing
    # if vote_token is not None:
    #     # This client hasn't voted, redirect to choices for election
    #     return redirect(url_for("election", election_id=election_id), code=303)
    election = admin.get_election_by_id(election_id)
    return render_template("result.html", results=election.results)


def confirm(candidat_name):
    message = "Votre vote pour " + candidat_name + " a été enregistré!"
    flash(message, "info")
    return redirect(url_for("index"))
