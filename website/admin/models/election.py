import uuid
from candidate import Candidate
from voter import Voter


class Election:
    def __init__(self, candidates, election_id=uuid.uuid4(), voters=None,
                 results=None):
        """
        Create a new instance of an election
        :param candidates: List of candidates
        :param election_id: unique uuid for the election
        :param voters: List of voters
        :param results: dict of candidate's name -> aggregate votes
        """
        if voters is None:
            voters = dict()
        if results is None:
            results = dict()
        self.candidates = candidates
        self.election_id = election_id
        self.voters = voters
        self.results = results

    @staticmethod
    def get_election(db, election_id):
        """
        Get an election from the database based on its id
        :param db: instance to the database object
        :param election_id: the id of the election
        :return: Election object
        """
        # TODO: To implement
        NotImplemented()

    @staticmethod
    def get_all_elections(db):
        """
        Get a list of all the elections in the database
        :param db: instance to the database object TODO: is it an obj or just the connection?
        :return: List[Election]
        """
        # TODO: To implement
        NotImplemented()

    @staticmethod
    def delete_election(db, election_id):
        """
        Delete an election from the database based on its id
        :param db: instance to the database object
        :param election_id: the id of the election
        """
        # TODO: To implement
        NotImplemented()
