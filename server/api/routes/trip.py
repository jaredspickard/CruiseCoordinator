from flask import request, make_response
from flask_login import (
    current_user as current_cruiser,
    logout_user as logout_cruiser,
    login_required
)

from server.api.utils.trip import TripUtils

from app import routes_bp


@routes_bp.route('/trips/list', methods=['GET'])
@login_required
def list_trips():
    """ API to list the trips for the logged-in cruiser. """
    try:
        trips = TripUtils.get_trips_by_cruiser_id(current_cruiser.id)
    except Exception as e:
        print(str(e))
        trips = []
    return make_response({'trips': trips})


@routes_bp.route('/trips/create', methods=['POST'])
@login_required
def create_trip():
    try:
        req = request.get_json(force=True)
        cruiser_id = current_cruiser.id
        trip_name = req.get('trip_name', 'default_trip_name')
        trip = TripUtils.create_trip(cruiser_id, trip_name)
        ret = {'trip': trip}
    except Exception as e:
        print(str(e))
        ret = {'trip': None}
    return ret, 200


@routes_bp.route('/trips/update', methods=['POST'])
@login_required
def update_trip():
    try:
        req = request.get_json(force=True)
        trip_id = req.get('trip_id')
        updated_data = req.get('trip_data')
        TripUtils.update_trip(trip_id, updated_data)
    except Exception as e:
        print(str(e))
    return make_response({'trip': {}})


@routes_bp.route('/trips/delete', methods=['DELETE'])
@login_required
def delete_trip():
    try:
        # TODO: check if trip id should be in req data or in route
        req = request.get_json(force=True)
        trip_id = req.get('trip_id')
        # TODO: ensure only the coordinator can delete their own trips
        TripUtils.delete_trip(trip_id)
    except Exception as e:
        print(str(e))
    return make_response({'trip': {}})