from google.oauth2 import id_token
from google.auth.transport import requests

from api.models import Cruiser, ExternalAccount, Trip
from api import db#, guard


GOOGLE_CLIENT_ID = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'


class Services:
    """ Utils class for CruiseCoordinator backend. """

    @staticmethod
    def create_cruiser(username, email, password):
        """ Create a new Cruiser with the given credentials and log them in. """
        new_cruiser = Cruiser(username=username, email=email)
        # set the password
        new_cruiser.set_password(password)
        # TODO: add this cruiser to the db session and commit
        # TODO: log the cruiser in 

    @staticmethod
    def create_cruiser_external_account(username, email, external_id, external_type):
        """ Create a new Cruiser linked through their google account using the given credentials and log them in. """
        # create a new cruiser
        new_cruiser = Cruiser(username=username, email=email)
        # create an associated external_account
        new_external_account = ExternalAccount(cruiser_id=new_cruiser.id, external_id=external_id, external_type=external_type)
        # TODO: add these models to the session and commit
        # TODO: log the cruiser in

    @staticmethod
    def check_account_availability(external_id, external_type):
        """ Returns True if an external_account does NOT exist for the given params, False if one DOES exist. """
        return ExternalAccount.query.filter_by(external_id=external_id, external_type=external_type).first() is None

    @staticmethod
    def get_google_user_id(token):
        """ Fetch Google User ID from the given token. """
        id_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        print(id_info)
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
        jwt = None#guard.encode_jwt_token(cruiser)
        return jwt

    @staticmethod
    def create_trip(cruiser_id, trip_name):
        trip = Trip(coordinator_id=cruiser_id, trip_name=trip_name)
        print(trip)
        db.session.add(trip)
        db.session.commit()
        return trip
