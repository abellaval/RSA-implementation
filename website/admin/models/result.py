class Result:
    def __init__(self, candidate_name, votes):
        self.candidate_name = candidate_name
        self.votes = votes

    @staticmethod
    def get_result_for_candidate(db, election_id, candidate_name):
        """
        Get the result for an individual candidate for an election
        :param db: instance of the database
        :param election_id: id of the election
        :param candidate_name: name of the candidate
        :return: Result object
        """
        # TODO: To implement
        NotImplemented()

    @staticmethod
    def get_results_for_election(db, election_id):
        """
        Get all the results for an election
        :param db: instance of the database
        :param election_id: id of the election
        :return: List[Result]
        """
        # TODO: To implement
        NotImplemented()