from website.admin import db


class Election(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(240), nullable=True)
    candidates = db.relationship("Candidate", backref="election")
    voters_participating = db.relationship("VoterParticipation",
                                           backref="election")
    results = db.relationship("Result", backref="election")
