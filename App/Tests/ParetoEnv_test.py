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
####################################################
    print(" =====Comparing chains...")
    print("Chain 1  is: "+ str(pareto.chain1))
    print("Expected is: "+ str(expectedChain1))
    print("-------")
    print("Chain 2  is: "+ str(pareto.chain2))
    print("Expected is: "+ str(expectedChain2))
    print("-------")
    print("Chain 3  is: "+ str(pareto.chain3))
    print("Expected is: "+ str(expectedChain3))
    print("-------")
    print("Chain 4  is: "+ str(pareto.chain4))
    print("Expected is: "+ str(expectedChain4))
    print("")
    print("PartoEnv is: "+ str(pareto.paretoEnv))
    print("Expected is: "+ str(expectedParetoEnv))
    print("")
    
    assert( str(pareto.chain1) == str(expectedChain1) ) 
    assert( str(pareto.chain2) == str(expectedChain2) ) 
    assert( str(pareto.chain3) == str(expectedChain3) ) 
    assert( str(pareto.chain4) == str(expectedChain4) ) 
    print(" =====Comparing Pareto Envelope...")
    assert( str(pareto.paretoEnv) == str(expectedParetoEnv) )

if __name__ == '__main__':
    main()
    print(" ===== Tests passed =====")