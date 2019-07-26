from flask import Flask
from flask_rq2 import RQ
from dobby_hardware.wheels import Wheels  # DON'T REMOVE
from dobby_hardware.camservo import Camservo  # DON'T REMOVE
from dobby_hardware.ultrasound import Ultrasonic  # DON'T REMOVE

rq = RQ()

def create_app():

    app = Flask(__name__)
    app.config.from_object('config')

    rq.init_app(app)
    
    from .api.wheels.views import wheels as wheelsapi
    from .api.cam.views import cam as camapi
    from .api.ultrasonic.views import path as pathapi

    app.register_blueprint(wheelsapi)
    app.register_blueprint(camapi)
    app.register_blueprint(pathapi)

    import web.jobs  # DON'T REMOVE

    return app
