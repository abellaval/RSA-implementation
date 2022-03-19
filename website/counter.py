import database
import crypto.RSA as RSA
from admin import Admin

counter = None


class Counter:
    def __init__(self):
        db = database.get_db()
        query = f"SELECT ek.election_id, ek.SK FROM election_keys ek"
        self.elections_secret_key = dict(
            (election_id, sk)
            for election_id, sk
            in db.execute(query)
        )

    @staticmethod
    def get_counter():
        global counter
        if counter is None:
            counter = Counter()
        return counter

    def recieve_votes(self, votes):
        self.count_votes(votes)

    def count_votes(self, votes):
        # count votes
        votes_by_election = dict()
        for election_id, choice, signature in votes:
            choice = int(RSA.D(
                choice,
                *(map(int, self.elections_secret_key[election_id].split('$')))
            ))
            if check_signature(choice, signature):
                election_votes = votes_by_election.setdefault(election_id, dict())
                candidate_votes_for_election = election_votes.setdefault(choice, 0)
                election_votes[choice] = candidate_votes_for_election + 1
        # save to DB
        db = database.get_db()
        for election_id, candidates_votes in votes_by_election.items():
            for candidate, new_votes_for_candidate in candidates_votes.items():
                query = f"""
                UPDATE result
                SET vote_count = vote_count + {new_votes_for_candidate}
                FROM (
                         SELECT cie.id
                         FROM candidate_in_election cie
                         WHERE election_id = {election_id}
                           AND vote_number = {candidate}
                     ) AS lookup
                WHERE lookup.id = result.election_candidate_id
                """
                db.execute(query)
        db.commit()


def check_signature(original_msg, signature):
    admin = Admin.get_admin()
    e, N = (map(int, admin.signature_secret_key.split('$')))
    decrypted_signature = RSA.E(signature, e, N)
    return True if decrypted_signature == original_msg else False
