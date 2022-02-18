from flask import Flask
import views
import api
import database

app = Flask(__name__)

app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/api/fingerprint/", view_func=api.fingerprint)
app.teardown_appcontext_funcs.append(database.clone_connection)
