from flask import Flask, render_template
from website.admin.database import Database
from website.admin.config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())
db = Database.init(app)

# importing the routes from the views, must be after the app init
from website.admin.views.index import *
