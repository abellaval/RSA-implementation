class Candidate:
    def __init__(self, name, number, description=""):
        """
        Create a new candidate object
        :param name: the name of the candidate
        :param number: the number used for his vote
        :param description: a short description about the candidate
        """
        self.name = name
        self.number = number
        self.description = description

    @staticmethod
    def get_candidate(db, election_id, candidates_name):
        """
        Get candidate from database based on the election and the name
        :param db: the database object
        :param election_id: the id of the election
        :param candidates_name: the name of the candidate
        :return: Candidate object
        """
        # TODO: To Implement
        NotImplemented()

    @staticmethod
    def get_all_candidates(db, election_id):
        """
        Get all the candidates that participate in the election
        with election_id
        :param db: the database object
        :param election_id: the id of the election
        :return: List[Candidates]
        """
        # TODO: To Implement
        NotImplemented()
