from website.client import app
from flask import request, Response
from website.client.controllers.fingerprint import generate_fingerprint
from datetime import datetime, timedelta


@app.route("/fingerprint/", methods=["POST"])
def fingerprint():
    # TODO: Add cookie to server side
    _fingerprint = generate_fingerprint(request)
    ttl_sec = 24*60*60
    response = Response(
        headers=[
            ("Set-Cookie",
             f"fingerprint={_fingerprint}; HttpOnly; Secure; SameSite=Strict; Max-Age={ttl_sec};"),
            ("Content-Type", "application/json")
        ]
    )
    return response
