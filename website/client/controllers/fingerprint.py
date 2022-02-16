from hashlib import sha256
from flask import Request


def generate_fingerprint(request: Request):
    visitor_id = request.get_json()
    hashed_ip = sha256(request.remote_addr.encode("ascii")).hexdigest()
    hashed_port = sha256(str(request.environ.get(
        "REMOTE_PORT")).encode("ascii")).hexdigest()
    return f"{visitor_id}@{hashed_ip}:{hashed_port}"
