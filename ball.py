# pymunk imports
import pymunk

from constants import *


class Ball(object):
    """
    This class implements a pool ball.
    """

    def __init__(self, x, y, **kwargs):
        self.mass = 10
        self.radius = 5.7 / 2 * SCALE_FACTOR
        self.inertia = pymunk.moment_for_circle(
            self.mass, 0, self.radius, (0, 0))

        self.body = pymunk.Body(self.mass, self.inertia)
        self.body.position = x, y

        self.shape = pymunk.Circle(self.body, self.radius, (0, 0))
        self.shape.elasticity = 0.95
        self.shape.friction = 0.9
