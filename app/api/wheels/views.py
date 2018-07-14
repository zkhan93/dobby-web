from flask import Blueprint, jsonify
from app import Wheels
from app.jobs.wheel_job import continious_movement

wheels = Blueprint('wheels_api_app', __name__, url_prefix='/api/wheels')


@wheels.route('/back/<float:secs>', defaults={'secs': 1.0})
@wheels.route('/back')
def back(secs=1.0):
    with Wheels(35, 36, 37, 38) as w:
        w.move_back(secs)
    return jsonify(dict(res='success'))


@wheels.route('/forward', defaults={'secs': 1.0})
@wheels.route('/forward/<float:secs>')
def forward(secs=1.0):
    with Wheels(35, 36, 37, 38) as w:
        w.move_forward(secs)
    return jsonify(dict(res='success'))


@wheels.route('/right', defaults={'secs': 1.0})
@wheels.route('/right/<float:secs>')
def right(secs=1.0):
    with Wheels(35, 36, 37, 38) as w:
        w.turn_left(secs)
    return jsonify(dict(res='success'))


@wheels.route('/left', defaults={'secs': 1.0})
@wheels.route('/left/<float:secs>')
def left(secs=1.0):
    with Wheels(35, 36, 37, 38) as w:
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
