import website.models.candidate as candidate
import website.models.election as election
import website.models.result as result
import website.models.voter as voter

Candidate = candidate.Candidate
Election = election.Election
Result = result.Result
Voter = voter.Voter

candidate_1 = Candidate(1, "candidate_name_1")
candidate_2 = Candidate(2, "candidate_name_2")
candidate_3 = Candidate(3, "candidate_name_3")
candidate_4 = Candidate(4, "candidate_name_4")
candidate_5 = Candidate(5, "candidate_name_5")
candidate_6 = Candidate(6, "candidate_name_6")
candidate_7 = Candidate(7, "candidate_name_7")

all_candidates = [candidate_1, candidate_2, candidate_3, candidate_4, candidate_5, candidate_6, candidate_7]

election_1 = Election(1, "election_name_1", "description_1",
                      [(candidate_1, 1),
                       (candidate_2, 2),
                       (candidate_3, 3)],
                      [])
election_1.results = [
    Result(election_1.id, candidate_1, 3),
    Result(election_1.id, candidate_2, 8),
    Result(election_1.id, candidate_3, 5)
]

election_2 = Election(2, "Pokemon starter", "Choose your pokemon",
                      [(candidate_4, 1),
                       (candidate_5, 2),
                       (candidate_6, 3)], [])

election_3 = Election(3, "You have no choice", "Modern democracy",
                      [(candidate_7, 1)], [])

all_elections = [election_1, election_2, election_3]
