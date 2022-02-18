class VoterParticipation:
    def __init__(self, election, fingerprint, vote_token, is_signed):
        self.election = election
        self.fingerprint = fingerprint
        self.vote_token = vote_token
        self.is_signed = is_signed
