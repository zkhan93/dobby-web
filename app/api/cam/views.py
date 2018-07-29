from flask import Blueprint, jsonify
from app import Camservo
import app

cam = Blueprint('cam_api_app', __name__, url_prefix='/api/cam')

# upright uphcenter upleft vcenterright vcenterhcenter vcenterleft
gpio_pins = app.config.get('CAMSERVO_GPIO')


@cam.route('/<string:direction>')
def move(direction):
    if direction in 'upright uphcenter upleft vcenterright vcenterhcenter vcenterleft'.split():
        with Camservo(*gpio_pins) as camservo:
            getattr(camservo, direction)()
        return jsonify(dict(res='success'))
    else:
        return jsonify(dict(res='fail', message='No such direction'))
