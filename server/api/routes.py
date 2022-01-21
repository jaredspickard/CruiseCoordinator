from flask import request, make_response
from flask_login import (
    current_user as current_cruiser,
    login_user as login_cruiser,
    logout_user as logout_cruiser,
    login_required
)

from api import app
from api.services import Services


GOOGLE = 'GOOGLE'


@app.route('/api/register', methods=['POST'])
def register():
    """ Register a new Cruiser Account without an external account. """
    try:
        req = request.get_json(force=True)
        username = req.get('username')
        email = req.get('email')
        password = req.get('password')
        Services.create_cruiser(username, email, password=password)
    except Exception as e:
        print(str(e))
    return make_response({})


@app.route('/api/external_account/available/google/<token>', methods=['GET'])
def google_account_availability(token):
    """ Check whether or not an external_account can be created for the given google account.
    
    If an external_account can be created, return the google_user_id. """
    try:
        external_id = Services.get_google_user_id(token)
        account_available = Services.check_account_availability(external_id, GOOGLE)
    except Exception as e:
        print(str(e))
        external_id = None
        account_available = False
    return make_response({
        'available': account_available,
        'external_id': external_id
    })
        


@app.route('/api/register/google', methods=['POST'])
def register_google():
    """ Register a new Cruiser Account using a Google Login. """
    try:
        req = request.get_json(force=True)
        username = req.get('username')
        email = req.get('email')
        google_user_id = req.get('google_user_id')
        Services.create_cruiser_external_account(username, email, google_user_id, GOOGLE)
    except Exception as e:
        print(str(e))
    return make_response({})


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


@app.route('/api/login/google', methods=['POST'])
def login_google():
    """ Logs a Cruiser in using the given username/google_user_id. """



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
