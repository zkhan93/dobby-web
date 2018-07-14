from app import rq, Wheels

max_duration = 10


@rq.job
def continious_movement(direction):
    for _ in range(3):
        with Wheels(35, 36, 37, 38) as wheels:
            attr = getattr(wheels, direction)
            if callable(attr):
                attr()
            else:
                print 'no such direction'
