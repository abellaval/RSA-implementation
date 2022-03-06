import sqlite3
from flask import g

DATABASE_PATH = "website/database.sqlite"


def get_db(path=DATABASE_PATH):
    db = getattr(g, "database", None)
    if db is None:
        db = g.database = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    return db


def clone_connection(exception):
    db = getattr(g, "database", None)
    if db is not None:
        db.close()
        g.database = None


if __name__ == "__main__":
    from website.app import app
    import crypto.RSA as RSA
    from admin import Admin

    with app.app_context():
        db = get_db("database.sqlite")
        # create the schema
        print("Creating Schema...", end="")
        with app.open_resource("schema.sql", mode='r') as f:
            db.executescript(f.read())
        print("Done")
        # db.commit()
        # insert data
        print("Inserting data...")
        with app.open_resource("dummy_inserts.sql", mode='r') as f:
            db.executescript(f.read())
        print("Done")
        # create keys
        print("Creating keys...")
        admin = Admin.get_admin()
        all_elections = admin.get_all_elections()
        k = 32
        values = ""
        for election in all_elections:
            sk, pk, _, _, _, _ = RSA.KeyGen(k)
            sk = f"{sk[0]}${sk[1]}"
            pk = f"{pk[0]}${pk[1]}"
            values += f"({election.id},'{sk}','{pk}'),"
        values = values[:-1] + ";"
        query = f"""
        INSERT INTO election_keys(election_id, SK, PK)
        VALUES {values}
        """
        db.execute(query)
        print("Done")
        db.commit()
