import pymunk
import logging

class Table(object): 
	def __init__(self, params): 
		self.height = params.get('height')
		self.length = params.get('length')
		self.padding = params.get('padding')
		self.static_body = params.get('static_body')

	def toList(self): 
		static_lines = [pymunk.Segment(self.static_body, (19, 19), (0, 100), 0.0),
                       pymunk.Segment(self.static_body, (100, 0), (100, 100), 0.0)]
		return static_lines