from werkzeug.serving import run_simple
from app import dispatcher_app


if __name__ == '__main__':
    run_simple('localhost', 5000, dispatcher_app, use_reloader=True, use_debugger=True,
               use_evalex=True)