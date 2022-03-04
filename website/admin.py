from flask import g
import models.dummy_data as dummy_data


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
        # TODO: Use DB instead
        return dummy_data.all_elections

    def get_election_by_id(self, election_id):
        # TODO: Use DB instead
        return next(filter(lambda election: election.id == election_id,
                           dummy_data.all_elections), None)
