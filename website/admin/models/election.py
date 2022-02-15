from website.admin import db


class Election(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidates = db.relationship("Candidate", backref="election")
    voters_participating = db.relationship("VoterParticipation",
                                           backref="election")
    results = db.relationship("Result", backref="election")
