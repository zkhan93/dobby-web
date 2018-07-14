from flask import Blueprint, jsonify
from app import Neck

cam = Blueprint('cam_api_app', __name__, url_prefix='/api/cam')

# upright uphcenter upleft vcenterright vcenterhcenter vcenterleft


@cam.route('/<string:direction>')
def move(direction):
    if direction in 'upright uphcenter upleft vcenterright vcenterhcenter vcenterleft'.split():
        with Neck(31, 32) as neck:
            getattr(neck, direction)()
        return jsonify(dict(res='success'))
    else:
        return jsonify(dict(res='fail', message='No such direction'))
