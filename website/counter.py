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
        # TODO: implement
        # count votes
        # save to DB
        # then notify admin of new results
        pass

