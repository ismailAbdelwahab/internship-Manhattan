#!/usr/bin/env python3
from Parser.CSVParser import CSVParser

from Data_structs.Point import Point
from Data_structs.OiAi import OiAi
from Data_structs.Strips import Strips

p1 = Point(5,0)
p2 = Point(2,1)
p3 = Point(3,3)
p4 = Point(1,4)

def getSetT():
    test_file = "Ressources/csv_points/test_strips.csv"
    terms = CSVParser.createSetTFromFile( test_file )
    return terms
def sortStripSet(stripsSet):
    stripsSet.sort( key = lambda tuple : tuple[1] )
    stripsSet.sort( key = lambda tuple : tuple[0] )

def main():
######## Initialization #############
    terms = getSetT()
    oiAi = OiAi( terms )
    oiAi.computeDictionaries()
    strips = Strips( terms, oiAi )

######## Expectations ###############
    expectedHS = [(p1,p2), (p2,p3), (p3,p4)]
    expectedVS = [(p1,p3), (p2,p3), (p2,p4)]

############ Tests ##################
    # Horizontal and Vertical strips
    strips.computeStrips() #TODO: implement this function
    sortStripSet( strips.HS )
    sortStripSet( expectedHS )
    sortStripSet( strips.VS )
    sortStripSet( expectedHS )
    print( "strips.HS => "+str(strips.HS))
    print( "expected  => "+str(expectedHS))
    print("----------------")
    print( "strips.VS => "+str(strips.VS))
    print( "expected  => "+str(expectedVS))
    assert( str(strips.HS) == str(expectedHS) )
    assert( str(strips.VS) == str(expectedVS) )

if __name__ == '__main__':
	main()