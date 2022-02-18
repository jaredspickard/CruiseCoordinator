from flask import request, make_response
from flask_login import (
    current_user as current_cruiser,
    logout_user as logout_cruiser,
    login_required
)

from server.api.utils.cruiser import CruiserUtils

from app import routes_bp


@routes_bp.route('/register', methods=['POST'])
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


@routes_bp.route('/login', methods=['POST'])
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


@routes_bp.route('/auth', methods=['GET'])
def check_auth():
    return make_response({'authenticated': current_cruiser.is_authenticated})


@routes_bp.route('/logout', methods=['GET'])
def logout():
    logout_cruiser()
    return make_response({'logged_out': True})


@login_required
@routes_bp.route('/cruisers/list', methods=['POST'])
def list_cruisers():
    """ Return a list of cruisers that match the given criteria. """
    cruisers = []
    try:
        req = request.get_json(force=True)
        filter_by = req.get('filter_by', [])
        sort_by = req.get('sort_by', [])
        cruisers = CruiserUtils.get_cruisers_by_criteria(filter_by, sort_by)
    except Exception as e:
        print(str(e))
    return cruisers
