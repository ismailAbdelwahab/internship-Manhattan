#!/usr/bin/env python3
from Parser.CSVParser import CSVParser

from Data_structs.Point import Point
from Data_structs.SetT import SetT
from Data_structs.OiAi import OiAi
from Data_structs.Strips import Strips

p1 = Point(0,5)
p2 = Point(2,1)
p3 = Point(3,3)
p4 = Point(1,4)

def getSetT():
    test_file = "Ressources/csv_points/test_strips.csv"
    terms = CSVParser.createSetTFromFile( test_file )
    return terms

def main():
######## Initialization #############
    terms = getSetT()
    OiAi = OiAi( terms )
    OiAi.computeDictionaries()
    strips = Strips( OiAi )

######## Expectations ###############
    expectedHS = [(p1,p2), (p2,p3), (p3,p4)]
    expectedVS = [(p4,p2), (p2,p3), (p3,p1)]

############ Tests ##################
    # Horizontal and Vertical strips
    OiAi.computeDictionaries()
    assert( str(strips.HS) == str(expectedHS) )
    assert( str(strips.VS) == str(expectedVS) )

if __name__ == '__main__':
	main()