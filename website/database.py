import sqlite3
from flask import g

DATABASE_PATH = "website/database.sqlite"


def get_db():
    db = getattr(g, "database", None)
    if db is None:
        db = g.database = sqlite3.connect(DATABASE_PATH)
    db.row_factory = sqlite3.Row
    return db


def clone_connection(exception):
    db = getattr(g, "database", None)
    if db is not None:
        db.close()
        g.database = None


if __name__ == "__main__":
    from website.app import app
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
