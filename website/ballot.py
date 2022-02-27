from copy import deepcopy

from flask import g

from website.admin import Admin
from website.counter import Counter


class Ballot:
    def __init__(self):
        self.content = []

    @staticmethod
    def get_ballot():
        ballot = getattr(g, "ballot", None)
        if ballot is None:
            ballot = g.ballot = Ballot()
        return ballot

    @staticmethod
    def tick(scheduler):
        # this allows use to use Flask context in function
        with scheduler.app.app_context():
            # TODO: remove the print on deploy
            print("Ballot tick")
            counter = Counter.get_counter()
            ballot = Ballot.get_ballot()
            counter.recieve_votes(deepcopy(ballot.content))
            ballot.content.clear()

    def put(self, election_id, vote_token, choice):
        admin = Admin.get_admin()
        admin.notify(election_id, vote_token)
        self.content.append((election_id, vote_token, choice))
