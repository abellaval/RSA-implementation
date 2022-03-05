from typing import Collection, Tuple

import website.models.candidate as candidate
import website.models.result as result
import website.models.voter as voter


class Election:
    Candidate = candidate.Candidate
    Result = result.Result
    Voter = voter.Voter
    CandidateForElection = Tuple[Candidate, int]

    def __init__(self,
                 id: int,
                 name: str,
                 description: str,
                 candidates: Collection[CandidateForElection],
                 results: Collection[Result] = None):
        if results is None:
            results = []
        self.id = id
        self.name = name
        self.description = description
        self.candidates = candidates
        self.results = results
