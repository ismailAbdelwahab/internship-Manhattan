#!/usr/bin/env python3
class ParetoEnv():
    def __init__(self, x, y):
        self.chain1 = []
        self.chain2 = []
        self.chain3 = []
        self.chain4 = []

        self.paretoEnv = []
##################### Chains construction ########################################
    def constructChain1(self, terms):
    	terms.sortIncXDescY()
    	previous = terms[0]
    	self.chain1.append( previous )
    	for i in range(1,n):
    		if terms[i].x > previous.x and terms[i].y == previous.y :
    			self.chain1.append( terms[i] )
    			previous = terms[i]
    		elif terms[i].x > previous.x and terms[i].y > previous.y :
    			temp = Point(previous.x, terms[i].y)
    			self.chain1 += [temp, terms[i]]
    			previous = terms[i]

    def constructChain2(self, terms):
    	pass
    def constructChain3(self, terms):
    	pass
    def constructChain4(self, terms):
    	pass

################ Pareto envelope construction #####################################
    def constructParetoEnv(self):
    	self.paretoEnv =  self.chain1 + self.chain2[1:] +\
    	                 self.chain3[1:] + self.chain4[1:-1]