from flask import request, make_response
from flask_login import (
    login_required
)

from server.api.utils.cruiser_relationship import CruiserRelationshipUtils
from server.api.utils.cruiser import CruiserUtils

from app import app


@login_required
@app.route('/api/friends/list', methods=['GET'])
def list_friends():
    """ List the current_cruisers friends. """
    try:
        # get ids of cruisers that have sent a friend request to current_cruiser 
        cruiser_ids = CruiserRelationshipUtils.get_friend_ids()
        # get list of cruisers for the above ids
        friends = CruiserUtils.get_cruisers_by_id(cruiser_ids)
    except Exception as e:
        print(str(e))
        friends = []
    return make_response({'friends': friends})


@login_required
@app.route('/api/friends/remove', methods=['POST'])
def remove_friend():
    """ Remove a Cruiser from the current_cruisers friends. """
    try:
        req = request.get_json(force=True)
        cruiser_id = req.get('cruiser_id')
        success = CruiserRelationshipUtils.remove_friend(cruiser_id)
    except Exception as e:
        print(str(e))
        success = False
    return make_response({'success': success})


@login_required
@app.route('/api/friends/requests/list', methods=['GET'])
def list_friend_requests():
    """ List friend requests for the current_cruiser. """
    # TODO: return the cruisers, not just the ids (look into blueprints)
    cruiser_ids = []
    try:
        # get ids of cruisers that have sent a friend request to current_cruiser 
        cruiser_ids = CruiserRelationshipUtils.get_friend_request_ids()
        # get list of cruisers for the above ids
        friend_requests = CruiserUtils.get_cruisers_by_id(cruiser_ids)
    except Exception as e:
        print(str(e))
    return make_response({'friend_requests': friend_requests})


@login_required
@app.route('/api/friends/requests/send', methods=['POST'])
def send_friend_request():
    """ Send a friend request to another Cruiser. """
    try:
        req = request.get_json(force=True)
        cruiser_id = req.get('cruiser_id')
        success = CruiserRelationshipUtils.send_friend_request(cruiser_id)
    except Exception as e:
        print(str(e))
        success = False
    return make_response({'success': success})


@login_required
@app.route('/api/friends/requests/accept', methods=['POST'])
def accept_friend_request():
    """ Accept a friend request from another Cruiser. """
    try:
        req = request.get_json(force=True)
        cruiser_id = req.get('cruiser_id')
        success = CruiserRelationshipUtils.accept_friend_request(cruiser_id)
    except Exception as e:
        print(str(e))
        success = False
    return make_response({'success': success})


@login_required
@app.route('/api/friends/requests/decline', methods=['POST'])
def decline_friend_request():
    """ Decline a friend request from another Cruiser. """
    try:
        req = request.get_json(force=True)
        cruiser_id = req.get('cruiser_id')
        success = CruiserRelationshipUtils.accept_friend_request(cruiser_id)
    except Exception as e:
        print(str(e))
        success = False
    return make_response({'success': success})
