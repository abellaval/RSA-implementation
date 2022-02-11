from flask import Flask, render_template, request, Response
from hashlib import sha256

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("home.html")


@app.route("/fingerprint/", methods=["POST"])
def fingerprint():
    # TODO: Add cookie to server side
    # TODO: Add expiration date (12~24h?)
    response = Response(
        headers=[
            ("Set-Cookie",
             "fingerprint={visitor_id}@{hashed_ip}; HttpOnly; Secure; SameSite=Strict".format(
                 visitor_id=request.get_json(),
                 hashed_ip=sha256(
                     request.remote_addr.encode("ascii")
                 ).hexdigest())),
            ("Content-Type", "application/json")
        ]
    )
    return response
