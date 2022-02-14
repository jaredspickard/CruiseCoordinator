# from flask import request, make_response
# from flask_login import (
#     current_user as current_cruiser,
#     logout_user as logout_cruiser,
#     login_required
# )

# from server.api.utils.cruiser import CruiserUtils
# from server.api.utils.trip import TripUtils

# from app import app


# @app.route('/api/register', methods=['POST'])
# def register():
#     """ Register a new Cruiser Account without an external account. """
#     try:
#         req = request.get_json(force=True)
#         email = req.get('email')
#         password = req.get('password')
#         success = CruiserUtils.create_cruiser_with_email(email, password)
#     except Exception as e:
#         print(str(e))
#         success = False
#     return make_response({'success': success})


# @app.route('/api/login', methods=['POST'])
# def login():
#     """ Log the cruiser in through their email. """
#     try:
#         req = request.get_json(force=True)
#         email = req.get('email')
#         password = req.get('password')
#         success = CruiserUtils.login_with_email(email, password)
#     except Exception as e:
#         print(str(e))
#         success = False
#     return make_response({'success': success})


# @app.route('/api/auth')
# def check_auth():
#     return make_response({'authenticated': current_cruiser.is_authenticated})


# @app.route('/api/logout')
# def logout():
#     logout_cruiser()
#     return make_response({'logged_out': True})


# @app.route('/api/trips/list', methods=['GET'])
# @login_required
# def list_trips():
#     """ API to list the trips for the logged-in cruiser. """
#     try:
#         trips = TripUtils.get_trips_by_cruiser_id(current_cruiser.id)
#     except Exception as e:
#         print(str(e))
#         trips = []
#     return make_response({'trips': trips})


# @app.route('/api/trips/create', methods=['POST'])
# @login_required
# def create_trip():
#     try:
#         req = request.get_json(force=True)
#         cruiser_id = current_cruiser.id
#         trip_name = req.get('trip_name', 'default_trip_name')
#         trip = TripUtils.create_trip(cruiser_id, trip_name)
#         ret = {'trip': trip}
#     except Exception as e:
#         print(str(e))
#         ret = {'trip': None}
#     return ret, 200


# @app.route('/api/trips/update', methods=['POST'])
# @login_required
# def update_trip():
#     try:
#         req = request.get_json(force=True)
#         trip_id = req.get('trip_id')
#         updated_data = req.get('trip_data')
#         TripUtils.update_trip(trip_id, updated_data)
#     except Exception as e:
#         print(str(e))
#     return make_response({'trip': {}})


# @app.route('/api/trips/delete', methods=['DELETE'])
# @login_required
# def delete_trip():
#     try:
#         # TODO: check if trip id should be in req data or in route
#         req = request.get_json(force=True)
#         trip_id = req.get('trip_id')
#         # TODO: ensure only the coordinator can delete their own trips
#         TripUtils.delete_trip(trip_id)
#     except Exception as e:
#         print(str(e))
#     return make_response({'trip': {}})
