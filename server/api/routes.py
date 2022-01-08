from api import app, guard
import flask
import flask_praetorian

from api.services import Services

# Set up some routes for the example
@app.route('/api/')
def home():
    return {"Hello": "World"}, 200


@app.route('/api/login/google', methods=['POST'])
def google_login():
    """ Logs in a Cruiser by parsing a POST request containing a Google Token ID. 
    
    If a Cruiser does not exist with the fetched (google) user_id, one is created. 
    Returns a JWT for the logged-in Cruiser. """
    try:
        req = flask.request.get_json(force=True)
        token = req.get('token', None)
        google_user_id = Services.get_google_user_id(token)
        cruiser_jwt = Services.get_cruiser_jwt_by_google_id(google_user_id)
        ret = {'access_token': cruiser_jwt}
    except ValueError:
        ret = {'access_token': None}
    return ret, 200


@app.route('/api/protected')
@flask_praetorian.auth_required
def protected():
    return {'message': 'successful access'}
    # return {'message': f'protected endpoint (allowed user {flask_praetorian.current_user().username})'}

  
# @app.route('/api/login', methods=['POST'])
# def login():
#     """
#     Logs a user in by parsing a POST request containing user credentials and
#     issuing a JWT token.
#     .. example::
#        $ curl http://localhost:5000/api/login -X POST \
#          -d '{"username":"Yasoob","password":"strongpassword"}'
#     """
#     req = flask.request.get_json(force=True)
#     username = req.get('username', None)
#     password = req.get('password', None)
#     user = guard.authenticate(username, password)
#     ret = {'access_token': guard.encode_jwt_token(user)}
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
#     print("refresh request")
#     old_token = request.get_data()
#     new_token = guard.refresh_jwt_token(old_token)
#     ret = {'access_token': new_token}
#     return ret, 200
  
  
# @app.route('/api/protected')
# @flask_praetorian.auth_required
# def protected():
#     """
#     A protected endpoint. The auth_required decorator will require a header
#     containing a valid JWT
#     .. example::
#        $ curl http://localhost:5000/api/protected -X GET \
#          -H "Authorization: Bearer <your_token>"
#     """
#     return {'message': f'protected endpoint (allowed user {flask_praetorian.current_user().username})'}