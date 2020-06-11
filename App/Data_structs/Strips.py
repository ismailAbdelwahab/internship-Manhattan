#!/usr/bin/env python3
class Strips():
	def __init__(self, terms, oiAi):
		self.terms = terms
		self.oiAi = oiAi
		self.HS = []
		self.VS = []

	def computeStrips(self):
		for point in self.terms.set:
			if point == self.O3( self.O1(point) ):
				self.HS.append( (point, self.O1(point)) )
			if point == self.O2( self.O4(point) ):
				self.HS.append( (point, self.O4(point)) )
			if point == self.A3( self.A1(point) ):
				self.VS.append( (point, self.A1(point)) )
			if point == self.A2( self.A4(point) ):
				self.VS.append( (point, self.A4(point)) )

	def O1(self, point):
		return self.oiAi.O1[point] if point is not None else None
	def O2(self, point):
		return self.oiAi.O2[point] if point is not None else None
	def O3(self, point):
		return self.oiAi.O3[point] if point is not None else None
	def O4(self, point):
		return self.oiAi.O4[point] if point is not None else None

	def A1(self, point):
		return self.oiAi.A1[point] if point is not None else None
	def A2(self, point):
		return self.oiAi.A2[point] if point is not None else None
	def A3(self, point):
		return self.oiAi.A3[point] if point is not None else None
	def A4(self, point):
		return self.oiAi.A4[point] if point is not None else None