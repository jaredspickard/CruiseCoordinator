from flask import Blueprint

routes_bp = Blueprint('routes', __name__)

from server.api.routes import (
    cruiser,
    cruiser_relationship,
    trip
)