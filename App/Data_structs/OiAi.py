#!/usr/bin/env python3

class OiAi():
	def __init__(self, terms):
		self.terms = terms
		self.O1 = {}; self.O2 = {}; self.O3 = {}; self.O4 = {}
		self.A1 = {}; self.A2 = {}; self.A3 = {}; self.A4 = {}

####################### Computing Oi ############################
	def computeO1(self):
		self.terms.sortIncYIncX()
		stack = []
		stack.append(self.terms.set[0])
		for point in self.terms.set[1:]:
			while len(stack) > 0 and stack[-1].x <= point.x:
				self.O1[ stack.pop() ] = point
			stack.append( point )
		while len(stack) > 0:
			self.O1[ stack.pop() ] = None
	def computeO2(self):
		self.terms.sortDecYIncX()
		stack=[]
		stack.append( self.terms.set[0] )
		for point in self.terms.set[1:]:
			while len(stack) > 0 and stack[-1].x <= point.x:
				self.O2[ stack.pop() ] = point
			stack.append( point )
		while len(stack) > 0:
			self.O2[ stack.pop() ] = None
	def computeO3(self):
		self.terms.sortDecYDecX()
		stack=[]
		stack.append( self.terms.set[0] )
		for point in self.terms.set[1:]:
			while len(stack) > 0 and stack[-1].x >= point.x:
				self.O3[ stack.pop() ] = point
			stack.append( point )
		while len(stack) > 0:
			self.O3[ stack.pop() ] = None
	def computeO4(self):
		self.terms.sortIncYDecX()
		stack=[]
		stack.append( self.terms.set[0] )
		for point in self.terms.set[1:]:
			while len(stack) > 0 and stack[-1].x >= point.x:
				self.O4[ stack.pop() ] = point
			stack.append( point )
		while len(stack) > 0:
			self.O4[ stack.pop() ] = None
####################### Computing Ai ############################
	def computeA1(self):
		self.terms.sortIncXIncY()
		stack = []
		stack.append(self.terms.set[0])
		for point in self.terms.set[1:]:
			while len(stack) > 0 and stack[-1].y <= point.y:
				self.A1[ stack.pop() ] = point
			stack.append( point )
		while len(stack) > 0:
			self.A1[ stack.pop() ] = None
	def computeA2(self):
		self.terms.sortIncXDecY()
		stack=[]
		stack.append( self.terms.set[0] )
		for point in self.terms.set[1:]:
			while len(stack) > 0 and stack[-1].y >= point.y:
				self.A2[ stack.pop() ] = point
			stack.append( point )
		while len(stack) > 0:
			self.A2[ stack.pop() ] = None
	def computeA3(self):
		self.terms.sortDecXDecY()
		stack=[]
		stack.append( self.terms.set[0] )
		for point in self.terms.set[1:]:
			while len(stack) > 0 and stack[-1].y >= point.y:
				self.A3[ stack.pop() ] = point
			stack.append( point )
		while len(stack) > 0:
			self.A3[ stack.pop() ] = None
	def computeA4(self):
		self.terms.sortDecXIncY()
		stack=[]
		stack.append( self.terms.set[0] )
		for point in self.terms.set[1:]:
			while len(stack) > 0 and stack[-1].y <= point.y:
				self.A4[ stack.pop() ] = point
			stack.append( point )
		while len(stack) > 0:
			self.A4[ stack.pop() ] = None
#########################################################################
	def computeDictionaries(self):
		self.computeO1(); self.computeO2(); self.computeO3(); self.computeO4()
		self.computeA1(); self.computeA2(); self.computeA3(); self.computeA4()