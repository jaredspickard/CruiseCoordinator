# from google.oauth2 import id_token
# from google.auth.transport import requests
from flask_login import (
    current_user as current_cruiser,
    login_user as login_cruiser
)

from server.api.models.cruiser import Cruiser

from app import db


class CruiserUtils:
    """ Utils class for cruiser-related functions. """

    @staticmethod
    def create_cruiser_with_email(email, password):
        """ Create a new Cruiser with the given credentials and log them in. """
        new_cruiser = Cruiser(email=email)
        # set the password
        new_cruiser.set_password(password)
        # add this cruiser to the db session and commit
        db.session.add(new_cruiser)
        db.session.commit()
        # log the cruiser in
        login_cruiser(new_cruiser)
        return True

    @staticmethod
    def login_with_email(email, password):
        """ Function to log a cruiser in using their email and password. """
        # fetch the cruiser entry
        cruiser = Cruiser.query.filter_by(email=email).first()
        # verify their password is correct
        valid_password = cruiser.check_password(password)
        if not valid_password:
            return False
        login_cruiser(cruiser)
        return True

    # @staticmethod
    # def get_google_user_id(token):
    #     """ Fetch Google User ID from the given token. """
    #     id_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
    #     google_user_id = id_info.get('sub')
    #     return google_user_id

    @staticmethod
    def get_cruisers_by_id(cruiser_ids):
        """ Get cruisers with the given cruiser_ids. """
        cruisers_raw = Cruiser.query.filter(
            Cruiser.id.in_(cruiser_ids)
        )
        return [c.serialize() for c in cruisers_raw]

    @staticmethod
    def get_cruisers_by_criteria(filter_by, sort_by):
        """ Get cruisers based on the given filter/sort params. """
        # TODO: use the criteria
        # currently returns all cruisers
        cruisers_raw = Cruiser.query.all()
        return [c.serialize() for c in cruisers_raw]
