#!/usr/bin/env python3
from Parser.CSVParser import CSVParser

from Data_structs.Point import Point
from Data_structs.OiAi import OiAi

p1 = Point(5,0)
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
    oiAi = OiAi( terms )
######## Expectations ###############
    expectedO1 = {p2:p3, p4:None, p3:None, p1:None}
    expectedO2 = {p4:p3, p2:p1, p3:p1, p1:None }
    expectedO3 = {p3:p2, p2:None, p1:None,p4:None}
    expectedO4 = {p1:p2, p3:p4, p2:p4, p4:None}
    
    expectedA1 = {p2:p3, p1:None, p3:None, p4:None}
    expectedA2 = {p4:p2, p3:p1, p2:p1, p1:None}
    expectedA3 = { p3:p2, p4:None, p2:None, p1:None}
    expectedA4 = {p1:p3, p2:p4, p3:p4, p4:None}
############ Tests ##################
    oiAi.computeDictionaries()
    assert( str(oiAi.O1) == str(expectedO1) )
    assert( str(oiAi.O2) == str(expectedO2) )
    assert( str(oiAi.O3) == str(expectedO3) )
    assert( str(oiAi.O4) == str(expectedO4) )

    assert( str(oiAi.A1) == str(expectedA1) )
    assert( str(oiAi.A2) == str(expectedA2) )
    assert( str(oiAi.A3) == str(expectedA3) )
    assert( str(oiAi.A4) == str(expectedA4) )

if __name__ == '__main__':
	main()