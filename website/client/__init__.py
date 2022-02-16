from flask import Flask, render_template, request, Response
from hashlib import sha256

app = Flask(__name__)

from website.client.views.index import *
from website.client.views.fingerprint import *
