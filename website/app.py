from flask import Flask
from flask_apscheduler import APScheduler
import views
import api
import database
from ballot import Ballot

app = Flask(__name__)
app.secret_key = "9aa15ada40490ed9549547aba8826752be22cd873e797eaaed98b0f07a17d490"

app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/election/<int:election_id>", view_func=views.election)
app.add_url_rule("/result/<int:election_id>", view_func=views.result)
app.add_url_rule("/calculator", view_func=views.calculator)
app.add_url_rule("/api/fingerprint/", view_func=api.fingerprint,
                 methods=["POST"])
app.add_url_rule("/api/make_choice/", view_func=api.make_choice,
                 methods=["POST"])
app.add_url_rule("/api/send_choice/", view_func=api.send_choice,
                 methods=["POST"])
app.add_url_rule("/api/refresh_results/", view_func=api.refresh_results,
                 methods=["GET"])

app.teardown_appcontext_funcs.append(database.clone_connection)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

scheduler.add_job("ballot_tick", lambda: Ballot.tick(scheduler),
                  trigger="interval",
                  seconds=2)

if __name__ == "__main__":
    app.run()
