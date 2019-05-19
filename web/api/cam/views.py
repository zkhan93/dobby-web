from flask import Blueprint, jsonify, current_app
from web import Camservo

cam = Blueprint('cam_api_app', __name__, url_prefix='/api/cam')

@cam.route('/<string:direction>')
def move(direction):
    # upright uphcenter upleft vcenterright vcenterhcenter vcenterleft
    gpio_pins = current_app.config.get('CAMSERVO_GPIO')
    if direction in 'upright uphcenter upleft vcenterright vcenterhcenter vcenterleft'.split():
        with Camservo(*gpio_pins) as camservo:
            getattr(camservo, direction)()
        return jsonify(dict(res='success'))
    else:
        return jsonify(dict(res='fail', message='No such direction'))
