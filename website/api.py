from flask import request, make_response, redirect, url_for
from fingerprint import generate_fingerprint
from website.admin import Admin
from website.ballot import Ballot


def fingerprint():
    _fingerprint = generate_fingerprint(request)
    ttl_sec = 24 * 60 * 60
    response = make_response()
    response.set_cookie("fingerprint", _fingerprint, max_age=ttl_sec,
                        httponly=True, secure=True)
    return response


def make_choice():
    # TODO: what is the name of the vote_token field on the html?
    election_id = request.args.get("election_id", type=int)
    blinded_choice = request.args.get("blinded_choice", type=int)
    if election_id is None or blinded_choice is None:
        # incorrect format of params
        return redirect(url_for("index"), code=303)
    vote_token = request.form.get("vote_token")
    if vote_token is None:
        # somehow we are trying to make a choice with no vote_token, deny and
        # redirect
        return redirect(url_for("election", election_id=election_id), code=303)
    # check if the vote_token is even inside the db and associatiated with
    # the fingerprint
    fingerprint = request.cookies.get("fingerprint")
    admin = Admin.get_admin()
    vote_token_from_db = admin.get_vote_token(election_id, fingerprint)
    if vote_token != vote_token_from_db:
        # the client tampered with his vote_token
        return redirect(url_for("election", election_id=election_id), code=303)
    # TODO: sign the blinded choice
    # TODO: send signed choice to client


def send_choice():
    election_id = request.args.get("election_id")
    choice = request.args.get("choice")
    vote_token = request.form.get("vote_token")
    if election_id is None or choice is None or vote_token is None:
        # incorrect format of params
        return redirect(url_for("index"), code=303)
    ballot = Ballot.get_ballot()
    ballot.put(election_id, vote_token, choice)
    return redirect(url_for("result", election_id=election_id), code=303)

