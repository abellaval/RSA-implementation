class Result:
    def __init__(self,
                 election_id: int,
                 candidate,
                 votes: int):
        self.election_id = election_id
        self.candidate = candidate
        self.votes = votes
