# from google.oauth2 import id_token
# from google.auth.transport import requests
from flask_login import (
    current_user as current_cruiser,
    login_user as login_cruiser
)

from api.models import Cruiser
from api import db


# GOOGLE_CLIENT_ID = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'


class CruiserServices:
    """ Utils class for cruiser-related functions. """

    @staticmethod
    def create_cruiser(email, password):
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
    def login_cruiser_with_email(email, password):
        """ Function to log a cruiser in using their email and password. """
        # fetch the cruiser entry
        cruiser = Cruiser.query.filter_by(email=email).first()
        # verify their password is correct
        valid_password = cruiser.check_password(password)
        if not valid_password:
            return False
        login_cruiser(cruiser)
        return True
