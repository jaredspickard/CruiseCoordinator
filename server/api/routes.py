from api import app
import flask
from google.oauth2 import id_token
from google.auth.transport import requests


GOOGLE_CLIENT_ID = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'


# Set up some routes for the example
@app.route('/api/')
def home():
    return {"Hello": "World"}, 200


@app.route('/api/authenticate/google', methods=['POST'])
def google_auth():
    """ Logs in a user by parsing a POST request containing a Google Token ID. """
    try:
        req = flask.request.get_json(force=True)
        token = req.get('token', None)
        id_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        user_id = id_info['sub']
        ret = {'user_id': user_id}
    except ValueError:
        ret = {'user_id': None}
    return ret, 200

  
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