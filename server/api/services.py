from google.oauth2 import id_token
from google.auth.transport import requests

from api.models import Cruiser
from api import db, guard


GOOGLE_CLIENT_ID = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'


class Services:
    """ Utils class for CruiseCoordinator backend. """

    @staticmethod
    def get_google_user_id(token):
        """ Fetch Google User ID from the given token. """
        id_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        google_user_id = id_info.get('sub')
        return google_user_id

    @staticmethod
    def get_or_create_cruiser(google_id):
        """ Get the Cruiser with the given google_id.
        
        If one does not exist, create one. """
        cruiser = Cruiser.query.filter_by(google_user_id=google_id).first()
        if not cruiser:
            cruiser = Cruiser(google_user_id=google_id)
            db.session.add(cruiser)
            db.session.commit()
        return cruiser

    @staticmethod
    def get_cruiser_jwt_by_google_id(google_id):
        """ Fetch JWT for the Cruiser with the given user_id as their Google ID. 
        
        Creates a Cruiser if one does not exist with this user_id. """
        cruiser = Services.get_or_create_cruiser(google_id)
        jwt = guard.encode_jwt_token(cruiser)
        return jwt
