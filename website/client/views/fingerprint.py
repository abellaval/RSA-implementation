from website.client import app
from flask import request, Response
from website.client.controllers.fingerprint import generate_fingerprint
from datetime import datetime, timedelta


@app.route("/fingerprint/", methods=["POST"])
def fingerprint():
    # TODO: Add cookie to server side
    _fingerprint = generate_fingerprint(request)
    expiration_date = datetime.utcnow() + timedelta(days=1)
    response = Response(
        headers=[
            ("Set-Cookie",
             f"fingerprint={_fingerprint}; HttpOnly; Secure; SameSite=Strict; Expires={expiration_date}"),
            ("Content-Type", "application/json")
        ]
    )
    return response
