#!/usr/bin/env python3
from Parser.CSVParser import CSVParser

from Data_structs.Point import Point
from Data_structs.SetT import SetT
from Data_structs.GridT import GridT
from Data_structs.ParetoEnv import ParetoEnv

# Bottom line
p1 = Point(1.5,1)
p2 = Point(4,1)
# Middle line
p3 = Point(2,3)
p4 = Point(4,3)
p5 = Point(5,3)
# Top line
p6 = Point(1.5,7.2)
p7 = Point(4,7.2)

def getSetT():
    test_file = "Ressources/csv_points/test.csv"
    terms = CSVParser.createSetTFromFile( test_file )
    return terms

def main():
    terms = getSetT()
    pareto = ParetoEnv( terms )
    pareto.constructParetoEnv()

    expectedChain1 = [p6, p7, p4, p5]
    expectedChain2 = [p5, p4, p2]
    expectedChain3 = [p2, p1]
    expectedChain4 = [p1, p6]

    expectedParetoEnv = [p6, p7, p4, p5, p4, p2, p1]
    #Check the creation of Si for i in (1..4)
    assert( cmp(pareto.chain1, expectedChain1))
    assert( cmp(pareto.chain2, expectedChain2))
    assert( cmp(pareto.chain3, expectedChain3))
    assert( cmp(pareto.chain4, expectedChain4))

    assert( cmp(pareto.paretoEnv, expectedParetoEnv))
if __name__ == '__main__':
	main()