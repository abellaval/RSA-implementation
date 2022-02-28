from flask import Flask
from flask_apscheduler import APScheduler
import views
import api
import database
from website.ballot import Ballot

app = Flask(__name__)
app.secret_key = "dummyKey" # testKey for the session

app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/election/<int:election_id>", view_func=views.election)
app.add_url_rule("/result/<int:election_id>", view_func=views.result)
app.add_url_rule("/confirm/<candidat_name>", view_func=views.confirm)
app.add_url_rule("/api/fingerprint/", view_func=api.fingerprint,
                 methods=["POST"])
app.add_url_rule("/api/make_choice/", view_func=api.make_choice,
                 methods=["POST"])
app.add_url_rule("/api/send_choice/", view_func=api.send_choice,
                 methods=["POST"])
app.teardown_appcontext_funcs.append(database.clone_connection)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

scheduler.add_job("ballot_tick", lambda: Ballot.tick(scheduler), trigger="interval",
                  seconds=5)

if __name__ == "__main__":
    app.run(debug=True)
