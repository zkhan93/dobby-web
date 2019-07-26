import os

DEBUG = os.getenv('DEBUG', False)

REDISTOGO_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

#WHEEL_GPIO = (35, 36, 37, 38)
WHEEL_GPIO = (22, 24, 16,18)
ULTRASONIC_GPIO = (7, 8)
#CAMSERVO_GPIO = (31, 32)
CAMSERVO_GPIO = (13, 15)
