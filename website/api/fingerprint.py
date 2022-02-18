from website.app import app
from website.controllers.fingerprint import generate_fingerprint
from flask import Request, Response, request


@app.route("/api/fingerprint/", methods=["POST"])
def fingerprint():
    # TODO: Add cookie to server side?
    _fingerprint = generate_fingerprint(request)
    ttl_sec = 24 * 60 * 60
    response = Response(
        headers=[
            ("Set-Cookie",
             f"fingerprint={_fingerprint}; HttpOnly; Secure; SameSite=Strict; Max-Age={ttl_sec};"),
            ("Content-Type", "application/json")
        ]
    )
    return response
