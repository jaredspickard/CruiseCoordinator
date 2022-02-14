# from google.oauth2 import id_token
# from google.auth.transport import requests
from flask_login import (
    current_user as current_cruiser,
    login_user as login_cruiser
)

from server.api.models.cruiser import (
    Cruiser,
    cruiser_relationships as CruiserRelationship
)
from app import db

# constants for cruiser relationships
FRIENDS = 'friends'
PENDING_FIRST_SECOND = 'pending_first_second'  # first has sent a friend request to second
PENDING_SECOND_FIRST = 'pending_second_first'


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
    def send_friend_request(cruiser_id):
        """ Function to send a friend request from the current_cruiser to the given cruiser_id. """
        # make sure a relationship doesn't already exist
        relationship = CruiserUtils.get_cruiser_relationship(current_cruiser.id, cruiser_id)
        if relationship:
            # a relationship already exists between these cruisers
            return False
        if current_cruiser.id < cruiser_id:
            first_id = current_cruiser.id
            second_id = cruiser_id
            rel_type = PENDING_FIRST_SECOND
        else:
            first_id = cruiser_id
            second_id = current_cruiser.id
            rel_type = PENDING_SECOND_FIRST
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
    def accept_friend_request(cruiser_id):
        """ Function to accept a friend request from the given cruiser_id. """
        # fetch the relationship with the given cruiser
        relationship = CruiserUtils.get_cruiser_relationship(current_cruiser.id, cruiser_id)
        if not relationship:
            # can't accept a friend request that doesn't exist
            return False
        # ensure the relationship is of the correct type (PENDING from cruiser_id)
        if current_cruiser.id < cruiser_id:
            if relationship.type != PENDING_SECOND_FIRST:
                return False
        else:
            if relationship.type != PENDING_FIRST_SECOND:
                return False
        # set the relationship type to FRIENDS
        relationship.type = FRIENDS
        db.session.add(relationship)
        db.session.commit()
        return True

    @staticmethod
    def decline_friend_request(cruiser_id):
        """ Function to decline a friend request from the cruiser_id. """
        # fetch the relationship with the given cruiser
        relationship = CruiserUtils.get_cruiser_relationship(current_cruiser.id, cruiser_id)
        if not relationship:
            # can't decline a friend request that doesn't exist
            return False
        # ensure the relationship is of the correct type (PENDING from cruiser_id)
        if current_cruiser.id < cruiser_id:
            if relationship.type != PENDING_SECOND_FIRST:
                return False
        else:
            if relationship.type != PENDING_FIRST_SECOND:
                return False
        # delete this relationship
        db.session.delete(relationship)
        db.session.commit()
        return True

    @staticmethod
    def remove_friend(cruiser_id):
        """ Function to remove the given cruiser as a friend. """
        relationship = CruiserUtils.get_cruiser_relationship(current_cruiser.id, cruiser_id)
        if relationship.type != FRIENDS:
            return False
        db.session.delete(relationship)
        db.session.commit()
        return True

    @staticmethod
    def get_cruiser_relationship(cruiser_id1, cruiser_id2):
        """ Function to fetch the cruiser_relationship for the given cruiser_ids. """
        # ensure first_id < second_id
        if cruiser_id1 < cruiser_id2:
            first_id = cruiser_id1
            second_id = cruiser_id2
        else:
            first_id = cruiser_id2
            second_id = cruiser_id1
        relationship = CruiserRelationship.query.filter_by(
            first_cruiser_id=first_id,
            second_cruiser_id=second_id
        ).first()
        return relationship
