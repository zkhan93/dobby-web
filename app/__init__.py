from flask import Flask
from flask_rq2 import RQ
from hardware.wheels import Wheels  # DON'T REMOVE
from hardware.camservo import Camservo  # DON'T REMOVE
from hardware.sensors.ultrasonic import Ultrasonic  # DON'T REMOVE



app = Flask(__name__)
rq = RQ(app)

app.config.from_object('config')

from api.wheels.views import wheels as wheelsapi
from api.cam.views import cam as camapi
from api.ultrasonic.views import path as pathapi

app.register_blueprint(wheelsapi)
app.register_blueprint(camapi)
app.register_blueprint(pathapi)

import jobs  # DON'T REMOVE