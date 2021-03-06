from server.api.models.trip import Trip

from app import db


class TripUtils:
    """ Utils class for trip-related functions. """

    @staticmethod
    def get_trips_by_cruiser_id(cruiser_id):
        """ Get a list of trips coordinated by the given cruiser (id). """
        trips_raw = Trip.query.filter_by(coordinator_id=cruiser_id).all()
        return [trip.serialize() for trip in trips_raw]

    @staticmethod
    def create_trip(cruiser_id, trip_name):
        """ Create a trip coordinated by the given cruiser_id and containing the given trip details. """
        trip = Trip(name=trip_name, coordinator_id=cruiser_id)
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