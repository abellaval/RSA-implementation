from hashlib import sha256
from flask import Request


def generate_fingerprint(request: Request):
    visitor_id = request.get_json()
    hashed_ip = sha256(request.remote_addr.encode("ascii")).hexdigest()
    # return f"{visitor_id}@{hashed_ip}"
    return str(hashed_ip)