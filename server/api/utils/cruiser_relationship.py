from operator import ge
from webbrowser import get
from flask_login import current_user as current_cruiser

from server.api.models.cruiser_relationship import CruiserRelationship
from server.api.models.cruiser import Cruiser

from app import db

# constants for cruiser relationships
FRIENDS = 'friends'
PENDING_FIRST_SECOND = 'pending_first_second'  # first has sent a friend request to second
PENDING_SECOND_FIRST = 'pending_second_first'


class CruiserRelationshipUtils:

    @staticmethod
    def get_friend_ids():
        """ Get ids of cruisers that are friends with the current_cruiser. """
        # get friends with id<current_cruiser.id
        first_ids = CruiserRelationshipUtils._get_cruiser_ids(
            current_cruiser.id, FRIENDS
        )
        # get friends with id>current_cruiser.id
        second_ids = CruiserRelationshipUtils._get_cruiser_ids(
            current_cruiser.id, FRIENDS, get_first_id=False
        )
        return first_ids + second_ids

    @staticmethod
    def get_friend_request_ids():
        """ Get ids of cruisers that have sent friend requests to the current_cruiser. """
        # get first_cruiser_ids that have sent a friend request to current_cruiser
        first_ids = CruiserRelationshipUtils._get_cruiser_ids(
            current_cruiser.id, PENDING_FIRST_SECOND
        )
        # get second_cruiser_ids that have sent a friend request to current_cruiser
        second_ids = CruiserRelationshipUtils._get_cruiser_ids(
            current_cruiser.id, PENDING_SECOND_FIRST, get_first_id=False
        )
        return first_ids + second_ids

    @staticmethod
    def _get_cruiser_ids(cruiser_id, rel_type, get_first_id=True):
        """ Helper function to get the ids that have the relationship type rel_type with the given cruiser_id.
        
        The get_first_id variable is used to determine whether to return first_id or second_id. """
        # get the first_cruiser_ids where the second_cruiser_id=cruiser_id
        if get_first_id:
            relationships = CruiserRelationship.query.with_entities(
                CruiserRelationship.first_cruiser_id
            ).filter_by(
                second_cruiser_id=cruiser_id,
                type=rel_type
            ).all()
            return [rel.first_cruiser_id for rel in relationships]
        else:          # get the second_cruiser_ids where the first_cruiser_id=cruiser_id
            relationships = CruiserRelationship.query.with_entities(
                CruiserRelationship.second_cruiser_id
            ).filter_by(
                first_cruiser_id=cruiser_id,
                type=rel_type
            ).all()
            return [rel.second_cruiser_id for rel in relationships]

    @staticmethod
    def send_friend_request(cruiser_id):
        """ Function to send a friend request from the current_cruiser to the given cruiser_id. """
        # make sure a relationship doesn't already exist
        relationship = CruiserRelationshipUtils.get_cruiser_relationship(current_cruiser.id, cruiser_id)
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
        relationship = CruiserRelationshipUtils.get_cruiser_relationship(current_cruiser.id, cruiser_id)
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
        relationship = CruiserRelationshipUtils.get_cruiser_relationship(current_cruiser.id, cruiser_id)
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
        relationship = CruiserRelationshipUtils.get_cruiser_relationship(current_cruiser.id, cruiser_id)
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
