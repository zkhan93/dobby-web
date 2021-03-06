from flask import Blueprint, jsonify, current_app
from web import Wheels
from web.jobs.wheel_job import continious_movement

wheels = Blueprint('wheels_api_app', __name__, url_prefix='/api/wheels')

def get_gpio_pins():
    return current_app.config.get('WHEEL_GPIO')

@wheels.route('/back/<float:secs>', defaults={'secs': 1.0})
@wheels.route('/back')
def back(secs=1.0):
    with Wheels(*get_gpio_pins()) as w:
        w.move_back(secs)
    return jsonify(dict(res='success'))


@wheels.route('/forward', defaults={'secs': 1.0})
@wheels.route('/forward/<float:secs>')
def forward(secs=1.0):
    with Wheels(*get_gpio_pins()) as w:
        w.move_forward(secs)
    return jsonify(dict(res='success'))


@wheels.route('/right', defaults={'secs': 0.5})
@wheels.route('/right/<float:secs>')
def right(secs=0.5):
    with Wheels(*get_gpio_pins()) as w:
        w.turn_left(secs)
    return jsonify(dict(res='success'))


@wheels.route('/left', defaults={'secs': 0.5})
@wheels.route('/left/<float:secs>')
def left(secs=0.5):
    with Wheels(*get_gpio_pins()) as w:
        w.turn_right(secs)
    return jsonify(dict(res='success'))


@wheels.route('/keep/<string:direction>')
def keep_moving(direction):
    if direction not in 'forward back right left'.split():
        return jsonify(dict(result='Invalid direction'))
    if direction in 'right left'.split():
        direction = 'turn_' + direction
    else:
        direction = 'move_' + direction
    continious_movement.queue(direction)
    return jsonify(dict(res='job queued'))
