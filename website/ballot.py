from flask import g

from website.admin import Admin


class Ballot:
    def __init__(self):
        self.content = []

    @staticmethod
    def get_ballot():
        ballot = getattr(g, "ballot", None)
        if ballot is None:
            # TODO: replace the None tuple with RSA keys
            ballot = g.ballot = Ballot()
        return ballot

    def put(self, election_id, vote_token, choice):
        admin = Admin.get_admin()
        admin.notify(election_id, vote_token)
        self.content.append((election_id, vote_token, choice))

