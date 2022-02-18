from flask_sqlalchemy import SQLAlchemy


class Database:
    @staticmethod
    def init(flask_app):
        return SQLAlchemy(flask_app)


if __name__ == "__main__":
    # Run this script to create empty database / init schema
    from website.app import db
    from website.models.election import *
    from website.models.candidate import *
    from website.models.voter_participation import *
    from website.models.result import *
    db.create_all()