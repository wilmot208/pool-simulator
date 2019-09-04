import pymunk
import logging
import math
from constants import *


class Table(object):
    def __init__(self, params):
        self.height = params.get('height')
        self.length = params.get('length')
        self.corner_pocket_width = params.get('corner_pocket_width')
        self.central_pocket_width = params.get('central_pocket_width')
        self.corner_pocket_depth = params.get('corner_pocket_depth')
        self.central_pocket_depth = params.get('central_pocket_depth')
        self.static_body = params.get('static_body')

    def getStaticLines(self):
        bottom_left = pymunk.Segment(self.static_body,
                                     (self.corner_pocket_width / 2 ** 0.5, 0),
                                     ((self.length - self.central_pocket_width) / float(2), 0),
                                     0.0)
        bottom_right = pymunk.Segment(self.static_body,
                                      ((self.length +
                                        self.central_pocket_width) /
                                       float(2), 0),
                                      (self.length -
                                       self.corner_pocket_width / 2 ** 0.5, 0),
                                      0.0)
        top_left = pymunk.Segment(self.static_body,
                                  (self.corner_pocket_width /
                                   2 ** 0.5, self.height),
                                  ((self.length - self.central_pocket_width) /
                                   float(2), self.height),
                                  0.0)
        top_right = pymunk.Segment(self.static_body,
                                   ((self.length + self.central_pocket_width) /
                                    float(2), self.height),
                                   (self.length - self.corner_pocket_width /
                                    2 ** 0.5, self.height),
                                   0.0)
        left_side = pymunk.Segment(self.static_body,
                                   (0, self.corner_pocket_width / 2 ** 0.5),
                                   (0, self.height -
                                    self.corner_pocket_width / 2 ** 0.5),
                                   0.0)
        right_side = pymunk.Segment(self.static_body,
                                    (self.length,
                                     self.corner_pocket_width / 2 ** 0.5),
                                    (self.length, self.height -
                                     self.corner_pocket_width / 2 ** 0.5),
                                    0.0)
        bottom_left_inner_corner_bottom = pymunk.Segment(self.static_body,
                                                         (self.corner_pocket_width /
                                                          2 ** 0.5, 0),
                                                         (self.corner_pocket_width / 2 ** 0.5 - self.corner_pocket_depth /
                                                          2 ** 0.5, -self.corner_pocket_depth / 2 ** 0.5),
                                                         0.0)
        bottom_left_inner_corner_left = pymunk.Segment(self.static_body,
                                                       (0, self.corner_pocket_width / 2 ** 0.5),
                                                       (-self.corner_pocket_depth / 2 ** 0.5, self.corner_pocket_width /
                                                        2 ** 0.5 - self.corner_pocket_depth / 2 ** 0.5),
                                                       0.0)
        bottom_right_inner_corner_bottom = pymunk.Segment(self.static_body,
                                                          (self.length -
                                                           self.corner_pocket_width / 2 ** 0.5, 0),
                                                          (self.length - self.corner_pocket_width / 2 ** 0.5 +
                                                           self.corner_pocket_depth / 2 ** 0.5, -self.corner_pocket_depth / 2 ** 0.5),
                                                          0.0)
        bottom_right_inner_corner_right = pymunk.Segment(self.static_body,
                                                         (self.length,
                                                          self.corner_pocket_width / 2 ** 0.5),
                                                         (self.length + self.corner_pocket_depth / 2 ** 0.5,
                                                          self.corner_pocket_width / 2 ** 0.5 - self.corner_pocket_depth / 2 ** 0.5),
                                                         0.0)
        top_left_inner_corner_top = pymunk.Segment(self.static_body,
                                                   (self.corner_pocket_width /
                                                    2 ** 0.5, self.height),
                                                   (self.corner_pocket_width / 2 ** 0.5 - self.corner_pocket_depth /
                                                    2 ** 0.5, self.height + self.corner_pocket_depth / 2 ** 0.5),
                                                   0.0)
        top_left_inner_corner_left = pymunk.Segment(self.static_body,
                                                    (0, self.height -
                                                     self.corner_pocket_width / 2 ** 0.5),
                                                    (-self.corner_pocket_depth / 2 ** 0.5, self.height -
                                                        self.corner_pocket_width / 2 ** 0.5 + self.corner_pocket_depth / 2 ** 0.5),
                                                    0.0)
        top_right_inner_corner_top = pymunk.Segment(self.static_body,
                                                    (self.length - self.corner_pocket_width /
                                                     2 ** 0.5, self.height),
                                                    (self.length - self.corner_pocket_width / 2 ** 0.5 + self.corner_pocket_depth /
                                                     2 ** 0.5, self.height + self.corner_pocket_depth / 2 ** 0.5),
                                                    0.0)
        top_right_inner_corner_right = pymunk.Segment(self.static_body,
                                                      (self.length, self.height -
                                                       self.corner_pocket_width / 2 ** 0.5),
                                                      (self.length + self.corner_pocket_depth / 2 ** 0.5, self.height -
                                                       self.corner_pocket_width / 2 ** 0.5 + self.corner_pocket_depth / 2 ** 0.5),
                                                      0.0)
        bottom_central_pocket_left = pymunk.Segment(self.static_body,
                                                    ((self.length - self.central_pocket_width) / float(2), 0),
                                                    ((self.length - self.central_pocket_width) / float(2) + self.central_pocket_depth * math.sin(math.radians(
                                                        CENTRAL_POCKET_ANGLE)), -self.central_pocket_depth * math.cos(math.radians(CENTRAL_POCKET_ANGLE))),
                                                    0.0)
        bottom_central_pocket_right = pymunk.Segment(self.static_body, 
                                                    ((self.length + self.central_pocket_width) / float(2), 0),
                                                    ((self.length + self.central_pocket_width) / float(2) - self.central_pocket_depth * math.sin(math.radians(
                                                        CENTRAL_POCKET_ANGLE)), -self.central_pocket_depth * math.cos(math.radians(CENTRAL_POCKET_ANGLE))), 
                                                    0.0)
        top_central_pocket_left = pymunk.Segment(self.static_body,
                                                    ((self.length - self.central_pocket_width) / float(2), self.height),
                                                    ((self.length - self.central_pocket_width) / float(2) + self.central_pocket_depth * math.sin(math.radians(
                                                        CENTRAL_POCKET_ANGLE)), self.height + self.central_pocket_depth * math.cos(math.radians(CENTRAL_POCKET_ANGLE))),
                                                    0.0)
        top_central_pocket_right = pymunk.Segment(self.static_body, 
                                                    ((self.length + self.central_pocket_width) / float(2), self.height),
                                                    ((self.length + self.central_pocket_width) / float(2) - self.central_pocket_depth * math.sin(math.radians(
                                                        CENTRAL_POCKET_ANGLE)), self.height + self.central_pocket_depth * math.cos(math.radians(CENTRAL_POCKET_ANGLE))), 
                                                    0.0)

        return [bottom_left, bottom_right, top_left, top_right, left_side, right_side, bottom_left_inner_corner_bottom, bottom_left_inner_corner_left, bottom_right_inner_corner_bottom,
                bottom_right_inner_corner_right, top_left_inner_corner_top, top_left_inner_corner_left, top_right_inner_corner_top, top_right_inner_corner_right, bottom_central_pocket_left,
                bottom_central_pocket_right, top_central_pocket_left, top_central_pocket_right]

    def shift(self, x, y):
        static_lines = self.getStaticLines()
        for line in static_lines:
            line.unsafe_set_endpoints(line.a + x, line.b + y)
        return static_lines
