from flask import Flask
from database import Database
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())
db = Database.init(app)

from views.index import *
from api.fingerprint import *

