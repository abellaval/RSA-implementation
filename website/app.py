from flask import Flask
import views
import api
import database

app = Flask(__name__)

app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/election/<int:election_id>", view_func=views.election)
app.add_url_rule("/result/<int:election_id>", view_func=views.result)
app.add_url_rule("/api/fingerprint/", view_func=api.fingerprint,
                 methods=["POST"])
app.add_url_rule("/api/make_choice/", view_func=api.make_choice,
                 methods=["POST"])
app.add_url_rule("/api/send_choice/", view_func=api.send_choice,
                 methods=["POST"])
app.teardown_appcontext_funcs.append(database.clone_connection)

if __name__ == "__main__":
    app.run(debug=True)
