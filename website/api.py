from flask import request, make_response, redirect, url_for, render_template
from fingerprint import generate_fingerprint
from website.admin import Admin
from website.ballot import Ballot
import crypto.RSA as RSA


def fingerprint():
    _fingerprint = generate_fingerprint(request)
    ttl_sec = 24 * 60 * 60
    response = make_response()
    response.set_cookie("fingerprint", _fingerprint, max_age=ttl_sec,
                        httponly=True, samesite="Strict")
    return response


def make_choice():
    election_id = request.form.get("election_id", type=int)
    blinded_choice = request.form.get("blinded_choice", type=int)
    if election_id is None or blinded_choice is None:
        # incorrect format of params
        return redirect(url_for("index"), code=303)
    vote_token = request.form.get("vote_token", type=str)
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
    admin_signing_expo, admin_signing_modulo = \
        admin.signature_public_key.split("$")
    signed_choice = RSA.D(blinded_choice,
                          int(admin_signing_expo),
                          int(admin_signing_modulo))
    return render_template("send_to_ballot.html",
                           election_id=election_id,
                           vote_token=vote_token,
                           signed_choice=signed_choice,
                           signing_modulo=admin_signing_modulo)


def send_choice():
    election_id = request.form.get("election_id", type=int)
    signed_choice = request.form.get("signed_choice", type=int)
    encrypted_choice = request.form.get("encrypted_choice", type=int)
    vote_token = request.form.get("vote_token", type=str)
    if election_id is None or signed_choice is None or vote_token is None:
        # incorrect format of params
        return redirect(url_for("index"), code=303)
    ballot = Ballot.get_ballot()
    admin = Admin.get_admin()
    # TODO: Not working and I don't know how to fix it
    # if check_signature(encrypted_choice, signed_choice,
    #                    *(map(int, admin.signature_secret_key.split('$')))):
    ballot.put(election_id, vote_token, encrypted_choice)
    return redirect(url_for("result", election_id=election_id), code=303)


def check_signature(original_msg, signature, e, N):
    decrypted_signature = RSA.E(signature, e, N)
    return True if decrypted_signature == original_msg else False


def refresh_results():
    fingerprint = request.cookies.get("fingerprint")
    admin = Admin.get_admin()
    # TODO: check if fingerprint has voted before giving results
    election = admin.get_election_by_id(request.args.get("election_id",
                                                         type=int))
    resp = dict(
        (result.candidate.id, result.votes) for result in election.results)
    return resp
