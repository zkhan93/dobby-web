from app import rq, Wheels
import app

max_duration = 10
gpio_pins = app.config.get('WHEEL_GPIO')


@rq.job
def continious_movement(direction):
    for _ in range(3):
        with Wheels(*gpio_pins) as wheels:
            attr = getattr(wheels, direction)
            if callable(attr):
                attr()
            else:
                print 'no such direction'
