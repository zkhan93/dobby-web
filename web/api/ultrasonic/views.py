from flask import Blueprint, jsonify, current_app
from web import Ultrasonic

path = Blueprint('path_api_app', __name__, url_prefix='/api/path')

@path.route('/')
def distance():
    # upright uphcenter upleft vcenterright vcenterhcenter vcenterleft
    gpio_pins = app.config.get('ULTRASONIC_GPIO')
    distance = None
    with Ultrasonic(*gpio_pins) as sensor:
        distance = sensor.measure()
    return jsonify(dict(res='success', distance=distance, unit='cms'))
