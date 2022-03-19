from hashlib import sha512

import database
from website.models.candidate import Candidate
from website.models.election import Election
from website.models.result import Result
import crypto.RSA as RSA

admin = None


class Admin:
    def __init__(self, signature_keypair):
        self.signature_secret_key, self.signature_public_key = signature_keypair
        self.elections_public_key = dict()

    @staticmethod
    def get_admin():
        global admin
        if admin is None:
            sk, pk, _, _, _, _ = RSA.KeyGen(k=256)
            sk = f"{sk[0]}${sk[1]}"
            pk = f"{pk[0]}${pk[1]}"
            admin = Admin((sk, pk))
        return admin

    def get_vote_token(self, election_id, fingerprint):
        db = database.get_db()
        vote_token_query = f"""
        SELECT fp.vote_token, s.is_signed
        FROM fingerprint fp
        JOIN signature s ON fp.vote_token = s.vote_token
        WHERE election_id = {election_id} AND fp.fingerprint = '{fingerprint}'
        """
        if (res := db.execute(vote_token_query).fetchone()) is None:
            # let's hope this is unique enough
            vote_token = sha512(
                (str(election_id) + fingerprint).encode("ascii")
            ).hexdigest()
            set_token_query = f"""
            INSERT INTO fingerprint (election_id, fingerprint, vote_token)
            VALUES ({election_id}, '{fingerprint}', '{vote_token}');
            """
            set_not_signed_query = f"""
            INSERT INTO signature (vote_token, is_signed)
            VALUES ('{vote_token}', {0});
            """
            db.execute(set_token_query)
            db.execute(set_not_signed_query)
            db.commit()
            return vote_token
        else:
            vote_token, is_signed = res
            return vote_token if not is_signed else None

    def notify(self, election_id, vote_token):
        """Notify admin that vote_token has voted for election"""
        db = database.get_db()
        query = f"""
        UPDATE signature
        SET is_signed=1
        WHERE vote_token = '{vote_token}'
        """
        db.execute(query)
        db.commit()

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

    def get_election_public_key(self, election_id):
        if (pk := self.elections_public_key.get(election_id)) is None:
            db = database.get_db()
            query = f"""
            SELECT ek.PK FROM election_keys ek WHERE ek.election_id = {election_id} 
            """
            pk = db.execute(query).fetchone()[0]
        return pk
