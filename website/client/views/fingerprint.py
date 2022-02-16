from website.client import app
from flask import request, Response
from website.client.controllers.fingerprint import generate_fingerprint


@app.route("/fingerprint/", methods=["POST"])
def fingerprint():
    # TODO: Add cookie to server side
    # TODO: Add expiration date (12~24h?)
    response = Response(
        headers=[
            ("Set-Cookie",
             "fingerprint={fingerprint}; HttpOnly; Secure; SameSite=Strict".format(
                 fingerprint=generate_fingerprint(request))
             ),
            ("Content-Type", "application/json")
        ]
    )
    return response
