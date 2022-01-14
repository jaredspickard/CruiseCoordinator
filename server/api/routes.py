from flask import request, make_response
from flask_login import (
    current_user as current_cruiser,
    login_user as login_cruiser,
    logout_user as logout_cruiser,
    login_required
)

from api import app
from api.services import Services


@app.route('/api/login', methods=['POST'])
def login():
    """ Logs in a Cruiser by parsing a POST request containing a Google Token ID. 
    
    If a Cruiser does not exist with the authenticated (google) user_id, one is created. 
    Returns a JWT for the logged-in Cruiser. """
    try:
        req = request.get_json(force=True)
        token = req.get('token')
        # validate the token using google auth (throws an error if invalid)
        google_user_id = Services.get_google_user_id(token)
        # get (or create) the associated cruiser
        cruiser = Services.get_or_create_cruiser(google_user_id)
        # login the user (in context of the session)
        login_cruiser(cruiser)
        resp = make_response({'logged_in': True})
    except Exception as e:
        resp = make_response({'logged_in': False, 'error_msg': str(e)})
    return resp


@app.route('/api/auth')
def check_auth():
    return make_response({'authenticated': current_cruiser.is_authenticated})


@app.route('/api/logout')
def logout():
    logout_cruiser()
    return make_response({'logged_out': True})


@app.route('/api/trips/create', methods=['POST'])
@login_required
def create_trip():
    try:
        req = request.get_json(force=True)
        cruiser_id = current_cruiser.id
        trip_name = req.get('trip_name', 'default_trip_name')
        trip = Services.create_trip(cruiser_id, trip_name)
        ret = {'trip': trip}
    except Exception as e:
        print(str(e))
        ret = {'trip': None}
    return ret, 200
