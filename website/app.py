from werkzeug.middleware.dispatcher import DispatcherMiddleware
from admin import app as admin_app
from client import app as client_app
from ballot import app as ballot_app
from counter import app as counter_app

dispatcher_app = DispatcherMiddleware(
    client_app,
    {"/admin": admin_app,
     "/ballot": ballot_app,
     "/counter": counter_app}
)
