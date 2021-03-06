from copy import deepcopy

from admin import Admin
from counter import Counter

ballot = None


class Ballot:
    def __init__(self):
        self.content = []

    @staticmethod
    def get_ballot():
        global ballot
        if ballot is None:
            ballot = Ballot()
        return ballot

    @staticmethod
    def tick(scheduler):
        # this allows use to use Flask context in function
        with scheduler.app.app_context():
            ballot = Ballot.get_ballot()
            if ballot.content:
                counter = Counter.get_counter()
                counter.recieve_votes(deepcopy(ballot.content))
                ballot.content.clear()

    def put(self, election_id, vote_token, choice, signature):
        admin = Admin.get_admin()
        admin.notify(election_id, vote_token)
        self.content.append((election_id, choice, signature))
