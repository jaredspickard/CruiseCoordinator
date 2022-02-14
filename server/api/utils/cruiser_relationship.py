from flask_login import current_user as current_cruiser

from server.api.models.cruiser_relationship import CruiserRelationship

from app import db

# constants for cruiser relationships
FRIENDS = 'friends'
PENDING_FIRST_SECOND = 'pending_first_second'  # first has sent a friend request to second
PENDING_SECOND_FIRST = 'pending_second_first'


class CruiserRelationshipUtils:

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
