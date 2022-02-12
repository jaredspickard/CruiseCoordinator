from google.oauth2 import id_token
from google.auth.transport import requests
from flask_login import (
    current_user as current_cruiser,
    login_user as login_cruiser
)

from server.api.models import (
    Cruiser,
    cruiser_relationships as CruiserRelationship,
    ExternalAccount,
    Trip
)
from server.api.constants import (
    FRIENDS,
    PENDING_FIRST_SECOND,
    PENDING_SECOND_FIRST
)
from app import db


GOOGLE_CLIENT_ID = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'


class CruiserServices:
    """ Utils class for cruiser-related functions. """

    @staticmethod
    def create_cruiser_email(email, password):
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
    def login_cruiser_email(email, password):
        """ Function to log a cruiser in using their email and password. """
        # fetch the cruiser entry
        cruiser = Cruiser.query.filter_by(email=email).first()
        # verify their password is correct
        valid_password = cruiser.check_password(password)
        if not valid_password:
            return False
        login_cruiser(cruiser)
        return True

    @staticmethod
    def send_friend_request(recipient_cruiser_id):
        """ Function to send a friend request from the current_cruiser to the given recipient_cruiser_id. """
        requesting_cruiser_id = current_cruiser.id
        first_id, second_id, rel_type = CruiserServices._get_first_second_type_relationship(requesting_cruiser_id, recipient_cruiser_id)
        # create a cruiser relationship
        new_relationship = CruiserRelationship(
            first_cruiser_id=first_id,
            second_cruiser_id=second_id,
            relationship_type=rel_type
        )
        db.session.add(new_relationship)
        db.session.commit()
        return True

    @staticmethod
    def accept_friend_request(requesting_cruiser_id):
        recipient_cruiser_id = current_cruiser.id
        first_id, second_id, rel_type = CruiserServices._get_first_second_type_relationship(requesting_cruiser_id, recipient_cruiser_id)
        # find the cruiser_relationship
        relationship = CruiserRelationship.query.filter_by(
            first_cruiser_id=first_id,
            second_cruiser_id=second_id
        ).first()
        # ensure that this is a valid operation
        if not relationship or relationship.type != rel_type:
            return False
        relationship.type = FRIENDS
        db.session.add(relationship)
        db.session.commit()
        return True

    @staticmethod
    def decline_friend_request(requesting_cruiser_id):
        recipient_cruiser_id = current_cruiser.id
        first_id, second_id, rel_type = CruiserServices._get_first_second_type_relationship(requesting_cruiser_id, recipient_cruiser_id)
        # find the cruiser_relationship
        relationship = CruiserRelationship.query.filter_by(
            first_cruiser_id=first_id,
            second_cruiser_id=second_id
        ).first()
        # ensure that this is a valid operation
        if not relationship or relationship.type != rel_type:
            return False
        # delete this relationship
        db.session.delete(relationship)
        db.session.commit()
        return True

    @staticmethod
    def _get_first_second_type_relationship(requesting_id, recipient_id):
        """ Helper function to get the appropriate first_cruiser_id, second_cruiser_id, and type for the given request/recipient relationship. """
        if requesting_id < recipient_id:
            first_cruiser_id = requesting_id
            second_cruiser_id = recipient_id
            relationship_type = PENDING_FIRST_SECOND
        else:
            first_cruiser_id = recipient_id
            second_cruiser_id = requesting_id
            relationship_type = PENDING_SECOND_FIRST
        return first_cruiser_id, second_cruiser_id, relationship_type

class TripServices:
    """ Utils class for trip-related functions. """

    @staticmethod
    def get_trips_by_cruiser_id(cruiser_id):
        """ Get a list of trips coordinated by the given cruiser (id). """
        trips_raw = Trip.query.filter_by(coordinator_id=cruiser_id).all()
        return [trip.serialize() for trip in trips_raw]

    @staticmethod
    def create_trip(cruiser_id, trip_name):
        """ Create a trip coordinated by the given cruiser_id and containing the given trip details. """
        trip = Trip(trip_name=trip_name, coordinator_id=cruiser_id)
        db.session.add(trip)
        db.session.commit()
        return trip.serialize()

    @staticmethod
    def update_trip(trip_id, updated_data):
        """ Update the given trip with the updated_data. """
        # TODO: add cruiser_id to verify that they are allowed to update this 
        return {}

    @staticmethod
    def delete_trip(trip_id):
        """ Delete the given trip. """
        # TODO: add cruiser_id to verify that this op can happen
        return True


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
