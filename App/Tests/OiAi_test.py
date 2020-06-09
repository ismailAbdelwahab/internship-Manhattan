#!/usr/bin/env python3
from Parser.CSVParser import CSVParser

from Data_structs.Point import Point
from Data_structs.SetT import SetT
from Data_structs.OiAi import OiAi

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

######## Expectations ###############
    expectedO1 = {p1:None, p2:p3, p3:None, p4:None}
    expectedO2 = {p1:None, p2:p1, p3:p1, p4:p3}
    expectedO3 = {p1:None, p2:None, p3:p2, p4:None}
    expectedO4 = {p1:p2, p2:p4, p3:p4, p4:None}
    
    expectedA1 = {p1:None, p2:p3, p3:None, p4:None}
    expectedA2 = {p1:None, p2:p1, p3:p1, p4:p2}
    expectedA3 = {p1:None, p2:None, p3:p2, p4:None}
    expectedA4 = {p1:p3, p2:p4, p3:p4, p4:None}
############ Tests ##################


if __name__ == '__main__':
	main()
