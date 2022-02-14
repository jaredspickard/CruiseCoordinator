from flask import request, make_response
from flask_login import (
    current_user as current_cruiser,
    logout_user as logout_cruiser,
    login_required
)

from server.api.utils.cruiser import CruiserUtils

from app import app


@app.route('/api/register', methods=['POST'])
def register():
    """ Register a new Cruiser Account without an external account. """
    try:
        req = request.get_json(force=True)
        email = req.get('email')
        password = req.get('password')
        success = CruiserUtils.create_cruiser_with_email(email, password)
    except Exception as e:
        print(str(e))
        success = False
    return make_response({'success': success})


@app.route('/api/login', methods=['POST'])
def login():
    """ Log the cruiser in through their email. """
    try:
        req = request.get_json(force=True)
        email = req.get('email')
        password = req.get('password')
        success = CruiserUtils.login_with_email(email, password)
    except Exception as e:
        print(str(e))
        success = False
    return make_response({'success': success})


@app.route('/api/auth')
def check_auth():
    return make_response({'authenticated': current_cruiser.is_authenticated})


@app.route('/api/logout')
def logout():
    logout_cruiser()
    return make_response({'logged_out': True})
