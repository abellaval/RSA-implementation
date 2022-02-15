from flask_sqlalchemy import SQLAlchemy


class Database:
    @staticmethod
    def init(flask_app):
        return SQLAlchemy(flask_app)


if __name__ == "__main__":
    # Run this script to create empty database / init schema
    from website.admin import db
    from website.admin.models.election import *
    from website.admin.models.candidate import *
    from website.admin.models.voter_participation import *
    from website.admin.models.result import *
    db.create_all()