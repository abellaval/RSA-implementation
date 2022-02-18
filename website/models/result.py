from website.app import db


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    election_id = db.Column(db.Integer, db.ForeignKey("election.id"),
                            nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.id"),
                             nullable=False)
    value = db.Column(db.Integer)
