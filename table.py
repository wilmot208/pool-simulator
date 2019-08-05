import pymunk
import logging

class Table(object): 
	def __init__(self, params): 
		self.height = params.get('height')
		self.length = params.get('length')
		self.padding = params.get('padding')
		self.corner_pocket_width = params.get('corner_pocket_width')
		self.central_pocket_width = params.get('central_pocket_width')
		self.static_body = params.get('static_body')

	def toList(self): 
		static_lines = [pymunk.Segment(self.static_body, (self.padding + self.corner_pocket_width / 2 ** 0.5, self.padding), ((self.length - self.central_pocket_width) / float(2), self.padding), 0.0),
                       pymunk.Segment(self.static_body, ((self.length + self.central_pocket_width) / float(2), self.padding), (self.length - self.padding - self.corner_pocket_width / 2 ** 0.5, self.padding), 0.0),
					   pymunk.Segment(self.static_body, (self.padding + self.corner_pocket_width / 2 ** 0.5, self.height - self.padding), ((self.length - self.central_pocket_width) / float(2), self.height - self.padding), 0.0),
                       pymunk.Segment(self.static_body, ((self.length + self.central_pocket_width) / float(2), self.height - self.padding), (self.length - self.padding - self.corner_pocket_width / 2 ** 0.5, self.height - self.padding), 0.0),
					   pymunk.Segment(self.static_body, (self.padding, self.padding + self.corner_pocket_width / 2 ** 0.5), (self.padding, self.height - self.padding - self.corner_pocket_width / 2 ** 0.5), 0.0),
					   pymunk.Segment(self.static_body, (self.length - self.padding, self.padding + self.corner_pocket_width / 2 ** 0.5), (self.length - self.padding, self.height - self.padding - self.corner_pocket_width / 2 ** 0.5), 0.0)]
		return static_lines