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
        resp = make_response({'message': 'success'})
    except Exception as e:
        resp = make_response({'message': str(e)})
    return resp


# @app.route('/api/login/google', methods=['POST'])
# def google_login():
#     """ Logs in a Cruiser by parsing a POST request containing a Google Token ID. 
    
#     If a Cruiser does not exist with the fetched (google) user_id, one is created. 
#     Returns a JWT for the logged-in Cruiser. """
#     try:
#         req = request.get_json(force=True)
#         token = req.get('token', None)
#         google_user_id = Services.get_google_user_id(token)
#         cruiser_jwt = Services.get_cruiser_jwt_by_google_id(google_user_id)
#         ret = {'access_token': cruiser_jwt}
#     except ValueError:
#         ret = {'access_token': None}
#     return ret, 200


# @app.route('/api/refresh', methods=['POST'])
# def refresh():
#     """
#     Refreshes an existing JWT by creating a new one that is a copy of the old
#     except that it has a refrehsed access expiration.
#     .. example::
#        $ curl http://localhost:5000/api/refresh -X GET \
#          -H "Authorization: Bearer <your_token>"
#     """
#     old_token = request.get_data()
#     new_token = guard.refresh_jwt_token(old_token)
#     ret = {'access_token': new_token}
#     return ret, 200


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
