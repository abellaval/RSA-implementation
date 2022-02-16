from flask import Flask

app = Flask(__name__)

from website.client.views.index import *
from website.client.api.fingerprint import *
