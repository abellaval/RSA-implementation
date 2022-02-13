class Voter:
    def __init__(self, fingerprint, voter_id):
        self.fingerprint = fingerprint
        self.voter_id = voter_id

    @staticmethod
    def get_voter(db, election_id, voter_id):
        """
        Get a voter based on his voter_id for a particular election
        :param db: the database object
        :param election_id: the id of the election
        :param voter_id: the id of the voter
        :return: Voter object
        """
        # TODO: To implement
        NotImplemented()

    @staticmethod
    def get_all_voters(db, election_id):
        """
        Get all the voters for a specific election
        :param db: the database object
        :param election_id: the id of the election
        :return: List[Election]
        """
        # TODO: To implement
        NotImplemented()

    @staticmethod
    def add_voter(db, election_id, fingerprint, voter_id):
        """
        Add a new voter for an election
        :param db: the database object
        :param election_id: the election id
        :param fingerprint: the fingerprint of the voter
        :param voter_id: the voter id
        """
        # TODO: To implement
        NotImplemented()