from flask import Blueprint, jsonify
from app import Path

path = Blueprint('path_api_app', __name__, url_prefix='/api/path')

# upright uphcenter upleft vcenterright vcenterhcenter vcenterleft


@path.route('/')
def distance():
    distance = None
    with Path(7, 8) as path:
        distance = path.measure()
    return jsonify(dict(res='success', distance=distance, unit='cms'))
