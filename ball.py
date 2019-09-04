# Python imports
import random

# pymunk imports
import pymunk


class Ball(object):
    """
    This class implements a pool ball.
    """

    def __init__(self):
        self.mass = 10
        self.radius = 8.55
        self.inertia = pymunk.moment_for_circle(
            self.mass, 0, self.radius, (0, 0))

        self.body = pymunk.Body(self.mass, self.inertia)
        self.x = random.randint(115, 350)
        self.body.position = self.x, 250

        self.shape = pymunk.Circle(self.body, self.radius, (0, 0))
        self.shape.elasticity = 0.95
        self.shape.friction = 0.9
