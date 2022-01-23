from flask import request, make_response
from flask_login import (
    current_user as current_cruiser,
    logout_user as logout_cruiser,
    login_required
)

from api import app
from api.services.cruisers import CruiserServices
from api.services.trips import TripServices


@app.route('/api/register', methods=['POST'])
def register():
    """ Register a new Cruiser Account without an external account. """
    try:
        req = request.get_json(force=True)
        email = req.get('email')
        password = req.get('password')
        CruiserServices.create_cruiser(email, password)
    except Exception as e:
        print(str(e))
    return make_response({})


@app.route('/api/login', methods=['POST'])
def login():
    """ Log the cruiser in through their email. """
    try:
        req = request.get_json(force=True)
        email = req.get('email')
        password = req.get('password')
        CruiserServices.login_cruiser(email, password)
    except Exception as e:
        print(str(e))
    return make_response({})


# @app.route('/api/external_account/available/google/<token>', methods=['GET'])
# def google_account_availability(token):
#     """ Check whether or not an external_account can be created for the given google account.
    
#     If an external_account can be created, return the google_user_id. """
#     try:
#         external_id = Services.get_google_user_id(token)
#         account_available = Services.check_account_availability(external_id, GOOGLE)
#     except Exception as e:
#         print(str(e))
#         external_id = None
#         account_available = False
#     return make_response({
#         'available': account_available,
#         'external_id': external_id
#     })
        


# @app.route('/api/register/google', methods=['POST'])
# def register_google():
#     """ Register a new Cruiser Account using a Google Login. """
#     try:
#         req = request.get_json(force=True)
#         username = req.get('username')
#         email = req.get('email')
#         google_user_id = req.get('google_user_id')
#         Services.create_cruiser_external_account(username, email, google_user_id, GOOGLE)
#     except Exception as e:
#         print(str(e))
#     return make_response({})


# @app.route('/api/login', methods=['POST'])
# def login():
#     """ Logs in a Cruiser by parsing a POST request containing a Google Token ID. 
    
#     If a Cruiser does not exist with the authenticated (google) user_id, one is created. 
#     Returns a JWT for the logged-in Cruiser. """
#     try:
#         req = request.get_json(force=True)
#         token = req.get('token')
#         # validate the token using google auth (throws an error if invalid)
#         google_user_id = Services.get_google_user_id(token)
#         # get (or create) the associated cruiser
#         cruiser = Services.get_or_create_cruiser(google_user_id)
#         # login the user (in context of the session)
#         login_cruiser(cruiser)
#         resp = make_response({'logged_in': True})
#     except Exception as e:
#         resp = make_response({'logged_in': False, 'error_msg': str(e)})
#     return resp


# @app.route('/api/login/google', methods=['POST'])
# def login_google():
#     """ Logs a Cruiser in using the given username/google_user_id. """



@app.route('/api/auth')
def check_auth():
    return make_response({'authenticated': current_cruiser.is_authenticated})


@app.route('/api/logout')
def logout():
    logout_cruiser()
    return make_response({'logged_out': True})


@app.route('/api/trips/list', methods=['GET'])
@login_required
def list_trips():
    """ API to list the trips for the logged-in cruiser. """
    try:
        trips = TripServices.get_trips_by_cruiser_id(current_cruiser.id)
    except Exception as e:
        print(str(e))
        trips = []
    return make_response({'trips': trips})


@app.route('/api/trips/create', methods=['POST'])
@login_required
def create_trip():
    try:
        req = request.get_json(force=True)
        cruiser_id = current_cruiser.id
        trip_name = req.get('trip_name', 'default_trip_name')
        trip = TripServices.create_trip(cruiser_id, trip_name)
        ret = {'trip': trip}
    except Exception as e:
        print(str(e))
        ret = {'trip': None}
    return ret, 200


@app.route('/api/trips/update', methods=['POST'])
@login_required
def update_trip():
    try:
        req = request.get_json(force=True)
        trip_id = req.get('trip_id')
        updated_data = req.get('trip_data')
        TripServices.update_trip(trip_id, updated_data)
    except Exception as e:
        print(str(e))
    return make_response({'trip': {}})


@app.route('/api/trips/delete', methods=['DELETE'])
@login_required
def delete_trip():
    try:
        # TODO: check if trip id should be in req data or in route
        req = request.get_json(force=True)
        trip_id = req.get('trip_id')
        # TODO: ensure only the coordinator can delete their own trips
        TripServices.delete_trip(trip_id)
    except Exception as e:
        print(str(e))
    return make_response({'trip': {}})
