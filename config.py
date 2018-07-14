import os

DEBUG = os.getenv('DEBUG', False)

REDISTOGO_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
