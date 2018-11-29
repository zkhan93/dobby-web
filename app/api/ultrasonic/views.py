from flask import Blueprint, jsonify
from app import Ultrasonic, app

path = Blueprint('path_api_app', __name__, url_prefix='/api/path')

# upright uphcenter upleft vcenterright vcenterhcenter vcenterleft
gpio_pins = app.config.get('ULTRASONIC_GPIO')


@path.route('/')
def distance():
    distance = None
    with Ultrasonic(*gpio_pins) as sensor:
        distance = sensor.measure()
    return jsonify(dict(res='success', distance=distance, unit='cms'))
