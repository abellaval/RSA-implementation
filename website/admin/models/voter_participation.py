from website.admin import db


class VoterParticipation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    election_id = db.Column(db.Integer, db.ForeignKey("election.id"),
                            nullable=False)
    fingerprint = db.Column(db.String(120), nullable=False)
    # TODO(victor): I am not sure about the type for the token (Int or String)?
    vote_token = db.Column(db.Integer, nullable=False)