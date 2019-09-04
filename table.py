import pymunk
import logging


class Table(object):
    def __init__(self, params):
        self.height = params.get('height')
        self.length = params.get('length')
        self.corner_pocket_width = params.get('corner_pocket_width')
        self.central_pocket_width = params.get('central_pocket_width')
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

        return [bottom_left, bottom_right, top_left,
                top_right, left_side, right_side]

    def shift(self, x, y):
        static_lines = self.getStaticLines()
        for line in static_lines:
            line.unsafe_set_endpoints(line.a + x, line.b + y)
        return static_lines
