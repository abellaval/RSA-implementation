from flask import g


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
