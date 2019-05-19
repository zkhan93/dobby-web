from web import rq, Wheels
from config import WHEEL_GPIO

gpio_pins = WHEEL_GPIO
max_duration = 10


@rq.job
def continious_movement(direction):
    for _ in range(3):
        with Wheels(*gpio_pins) as wheels:
            attr = getattr(wheels, direction)
            if callable(attr):
                attr()
            else:
                print('no such direction')
