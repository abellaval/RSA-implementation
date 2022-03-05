from flask import g
import database
from website.models.candidate import Candidate
from website.models.election import Election
from website.models.result import Result


class Admin:
    def __init__(self, signature_keypair):
        self.signature_secret_key, self.signature_public_key = signature_keypair

    @staticmethod
    def get_admin():
        admin = getattr(g, "admin", None)
        if admin is None:
            # TODO: replace the None tuple with RSA keys
            admin = g.admin = Admin((None, None))
        return admin

    def get_vote_token(self, election_id, fingerprint):
        # TODO: check in DB if fingerprint has already voted, if not return
        #  vote token, if already voted return None
        # FIXME: This is dummy data
        if election_id == 1:
            return 123
        else:
            return None

    def notify(self, election_id, vote_token):
        """Notify admin that vote_token has voted for election"""
        # TODO: implement
        pass

    def get_all_elections(self):
        db = database.get_db()
        election_query = """
        SELECT * 
        FROM election
        """
        all_elections = []
        for election_row in db.execute(election_query):
            election_id, election_name, election_desc = election_row
            candidate_query = f"""
            SELECT c.id, name, description, vote_number
            FROM candidate c
            JOIN candidate_in_election cie on c.id = cie.candidate_id
            WHERE cie.election_id = {election_id}
            """
            candidates_in_election = []
            for candidate_row in db.execute(candidate_query):
                candidates_in_election.append(
                    (Candidate(*candidate_row[:-1]), candidate_row[-1])
                )
            result_query = f"""
            SELECT candidate_id, vote_count
            FROM result r
            JOIN candidate_in_election cie ON r.election_candidate_id = cie.id
            WHERE election_id = {election_id}
            """
            results_for_election = []
            for result_row in db.execute(result_query):
                candidate_id, vote_count = result_row
                results_for_election.append(
                    Result(
                        election_id,
                        next(candidate for candidate, _ in
                             candidates_in_election
                             if candidate.id == candidate_id),
                        vote_count
                    )
                )
            all_elections.append(
                Election(
                    election_id,
                    election_name,
                    election_desc,
                    candidates_in_election,
                    results_for_election
                )
            )
        return all_elections

    def get_election_by_id(self, election_id):
        return next(filter(lambda election: election.id == election_id,
                           self.get_all_elections()), None)
