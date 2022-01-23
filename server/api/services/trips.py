from api.models import Trip
from api import db


class TripServices:
    """ Utils class for trip-related functions. """

    @staticmethod
    def get_trips_by_cruiser_id(cruiser_id):
        """ Get a list of trips coordinated by the given cruiser (id). """
        return []

    @staticmethod
    def create_trip(cruiser_id, trip_details):
        """ Create a trip coordinated by the given cruiser_id and containing the given trip details. """
        # TODO: look into unpacking params
        return {}

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
