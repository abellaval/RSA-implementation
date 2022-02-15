from website.admin import db


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    election_id = db.Column(db.Integer, db.ForeignKey("election.id"),
                            nullable=False)
    vote_number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(280), nullable=True)
