#!/usr/bin/env python3
class ParetoEnv():
    def __init__(self, x, y):
        self.chain1 = []
        self.chain2 = []
        self.chain3 = []
        self.chain4 = []

        self.paretoEnv = []

    def constructChain1(self):
    	pass
    def constructChain2(self):
    	pass
    def constructChain3(self):
    	pass
    def constructChain4(self):
    	pass

    def constructParetoEnv(self):
    	self.paretoEnv =  self.chain1 + self.chain2[1:] +\
    	                 self.chain3[1:] + self.chain4[1:-1]
def main():
	pass

if __name__ == '__main__':
	main()
