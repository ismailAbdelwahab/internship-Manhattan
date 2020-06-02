#!/usr/bin/env python3
class ParetoEnv():
    def __init__(self, terms):
    	self.terms = terms
        self.chain1 = []
        self.chain2 = []
        self.chain3 = []
        self.chain4 = []

        self.paretoEnv = []
##################### Chains construction ########################################
    def constructChain1(self): # North to East
    	self.terms.sortIncXDecY()
    	previous = self.terms[0]
    	self.chain1.append( previous )
    	for i in range(1,n):
    		if self.terms[i].x > previous.x and self.terms[i].y == previous.y :
    			self.chain1.append( self.terms[i] )
    			previous = self.terms[i]
    		elif self.terms[i].x > previous.x and self.terms[i].y < previous.y :
    			temp = Point(previous.x, self.terms[i].y)
    			self.chain1 += [temp, self.terms[i]]
    			previous = self.terms[i]

    def constructChain2(self): # East to South
    	self.terms.sortDecXDecY()
    	previous = self.terms[0]
    	self.chain2.append( previous )
    	for i in range(1,n):
    		if self.terms[i].x < previous.x and self.terms[i].y == previous.y:
    			self.chain2.append( self.terms[i] )
    			previous = self.terms[i]
    		elif self.terms[i].x < previous.x and self.terms[i].y < previous.y:
    			temp = Point(self.terms[i].x, previous.y)
    			self.chain2 += [temp, self.terms[i]]
    			previous = self.terms[i]

    def constructChain3(self): # South to West
    	self.terms.sortDecXIncY()
    	previous = self.terms[0]
    	self.chain3.append( previous )
    	for i in range(1,n):
    		if self.terms[i].x < previous.x and self.terms[i].y == previous.y:
    			self.chain3.append( self.terms[i] )
    			previous = self.terms[i]
    		elif self.terms[i].x < previous.x and self.terms[i].y > previous.y:
    			temp = Point(previous.x, self.terms[i].y)
    			self.chain3 += [temp, self.terms[i]]
    			previous = self.terms[i]

    def constructChain4(self): # West to North
    	self.terms.sortIncXIncY()
    	previous = self.terms[0]
    	self.chain4.append( previous )
    	for i in range(1,n):
	    	if self.terms[i].x > previous.x and self.terms[i].y == previous.y:
	    		self.chain4.append( self.terms[i] )
	    		previous = self.terms[i]
	    	elif self.terms[i].x > previous.x and self.terms[i].y > previous.y:
	    		temp = Point(self.terms[i].x, previous.y)
	    		self.chain4 += [temp, self.terms[i]]
	    		previous = self.terms[i]



################ Pareto envelope construction #####################################
    def constructParetoEnv(self):
    	self.constructChain1()
    	self.constructChain2()
    	self.constructChain3()
    	self.constructChain4()
    	self.paretoEnv =  self.chain1 + self.chain2[1:] +\
    	                 self.chain3[1:] + self.chain4[1:-1]