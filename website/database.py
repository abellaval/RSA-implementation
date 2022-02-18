import sqlite3
from flask import g
from app import app

DATABASE_PATH = "database.sqlite"


def get_db():
    db = getattr(g, "database", None)
    if db is None:
        db = g.database = sqlite3.connect(DATABASE_PATH)
    db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def clone_connection(exception):
    db = getattr(g, "database", None)
    if db is not None:
        db.close()
        g.database = None


if __name__ == "__main__":
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
