from flask import g


class Counter:
    def __init__(self, key_pair):
        self.content = []
        self.sk_key, self.pk_key = key_pair

    @staticmethod
    def get_counter():
        counter = getattr(g, "counter", None)
        if counter is None:
            # TODO: replace the None tuple with RSA keys
            counter = g.admin = Counter((None, None))
        return counter

    def recieve_votes(self, votes):
        for vote in votes:
            self.content.append(vote)
        self.count_votes()

    def count_votes(self):
        # TODO: implement
        # count votes
        # save to DB
        # then notify admin of new results
        pass

