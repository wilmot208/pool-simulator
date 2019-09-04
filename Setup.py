"""This example spawns (bouncing) balls randomly on a L-shape constructed of 
two segment shapes. Not interactive.
"""

__version__ = "$Id:$"
__docformat__ = "reStructuredText"

# Python imports
import random

# Library imports
import pygame
from pygame.key import *
from pygame.locals import *
from pygame.color import *

# pymunk imports
import pymunk
import pymunk.pygame_util

from ball import Ball
from table import Table

from constants import *

class PoolGame(object):
    """
    This class implements the setup for a game of pool.
    """

    def __init__(self):
        # Space
        self._space = pymunk.Space()
        self._space.gravity = (0.0, -981.0)

        # Physics
        # Time step
        self._dt = 1.0 / 60.0
        # Number of physics steps per screen frame
        self._physics_steps_per_frame = 1

        # pygame
        pygame.init()

        self._screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))
        self._clock = pygame.time.Clock()

        self._draw_options = pymunk.pygame_util.DrawOptions(self._screen)

        # Static barrier walls (lines) that the balls bounce off of
        self._add_static_scenery()

        # Balls that exist in the world
        self._balls = []

        # Execution control and time until the next ball spawns
        self._running = True
        self._ticks_to_next_ball = 10

    def run(self):
        """
        The main loop of the game.
        :return: None
        """

        # Main loop
        while self._running:
            # Progress time forward
            for x in range(self._physics_steps_per_frame):
                self._space.step(self._dt)
            self._process_events()
            self._update_balls()
            self._clear_screen()
            self._draw_objects()
            pygame.display.flip()
            # Delay fixed time between frames
            self._clock.tick(50)
            pygame.display.set_caption("fps: " + str(self._clock.get_fps()))

    def _add_static_scenery(self):
        """
        Create the static bodies.
        :return: None
        """
        static_body = self._space.static_body
        static_lines = Table({"height": TABLE_HEIGHT, "length": TABLE_LENGTH, "corner_pocket_width": CORNER_POCKET_WIDTH,
                              "central_pocket_width": CENTRAL_POCKET_WIDTH, "corner_pocket_depth": CORNER_POCKET_DEPTH,
                              "central_pocket_depth": CENTRAL_POCKET_DEPTH, "static_body": static_body})
        static_lines = static_lines.shift(100, 100)
        for line in static_lines:
            line.elasticity = 0.95
            line.friction = 0.9
        self._space.add(static_lines)

    def _process_events(self):
        """
        Handle game and events like keyboard input. Call once per frame only.
        :return: None
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                self._running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                self._running = False
            elif event.type == KEYDOWN and event.key == K_p:
                pygame.image.save(self._screen, "bouncing_balls.png")

    def _update_balls(self):
        """
        Create/remove balls as necessary. Call once per frame only.
        :return: None
        """
        self._ticks_to_next_ball -= 1
        if self._ticks_to_next_ball <= 0:
            self._create_ball()
            self._ticks_to_next_ball = 100
        # Remove balls that fall below 100 vertically
        balls_to_remove = [
            ball for ball in self._balls if ball.body.position.y < -100]
        for ball in balls_to_remove:
            self._space.remove(ball, ball.body)
            self._balls.remove(ball)

    def _create_ball(self):
        """
        Create a ball.
        :return:
        """
        new_ball = Ball()
        self._add_ball(new_ball)

    def _add_ball(self, ball):
        """
        Add a ball to the space
        :return: None
        """
        self._space.add(ball.body, ball.shape)
        self._balls.append(ball.shape)

    def _clear_screen(self):
        """
        Clears the screen.
        :return: None
        """
        self._screen.fill(TABLE_COLOUR)
        background_image = pygame.image.load("table.png")
        self._screen.blit(background_image, [0, 0])

    def _draw_objects(self):
        """
        Draw the objects.
        :return: None
        """
        self._space.debug_draw(self._draw_options)


if __name__ == '__main__':
    game = PoolGame()
    game.run()
