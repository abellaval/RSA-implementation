from uuid import UUID


class Voter:
    def __init__(self, vote_token: UUID):
        self.vote_token = vote_token
