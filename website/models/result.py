import website.models.candidate as candidate


class Result:
    def __init__(self,
                 election_id: int,
                 candidate: candidate.Candidate,
                 votes: int):
        self.election_id = election_id
        self.candidate = candidate
        self.votes = votes
