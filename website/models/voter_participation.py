from website.app import db


class VoterParticipation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    election_id = db.Column(db.Integer, db.ForeignKey("election.id"),
                            nullable=False)
    fingerprint = db.Column(db.String(180), nullable=False)
    vote_token = db.Column(db.String(32), nullable=False)