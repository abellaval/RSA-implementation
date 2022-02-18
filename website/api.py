from flask import request, make_response
from fingerprint import generate_fingerprint


def fingerprint():
    _fingerprint = generate_fingerprint(request)
    ttl_sec = 24 * 60 * 60
    response = make_response()
    response.set_cookie("fingerprint", _fingerprint, max_age=ttl_sec,
                        httponly=True, secure=True)
    return response
