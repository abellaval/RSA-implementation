import database

counter = None


class Counter:
    def __init__(self, key_pair):
        self.content = []
        self.sk_key, self.pk_key = key_pair

    @staticmethod
    def get_counter():
        global counter
        if counter is None:
            # TODO: replace the None tuple with RSA keys
            counter = Counter((None, None))
        return counter

    def recieve_votes(self, votes):
        for vote in votes:
            self.content.append(vote)
        self.count_votes()

    def count_votes(self):
        # count votes
        votes = dict()
        for election_id, choice in self.content:
            # TODO: decrypt vote when RSA is implemented
            election_votes = votes.setdefault(election_id, dict())
            candidate_votes_for_election = election_votes.setdefault(choice, 0)
            election_votes[choice] = candidate_votes_for_election + 1
        # save to DB
        db = database.get_db()
        for election_id, candidates_votes in votes.items():
            for candidate, new_votes in candidates_votes.items():
                query = f"""
                UPDATE result
                SET vote_count = vote_count + {new_votes}
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

