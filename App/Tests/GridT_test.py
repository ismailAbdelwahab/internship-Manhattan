#!/usr/bin/env python3
from Data_structs.Point import Point
from Data_structs.SetT import SetT
from Data_structs.GridT import GridT
from Parser.CSVParser import CSVParser

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
    grid = GridT( terms )
    grid.computeGrid( terms )
    print("terms ==>" + str(terms) )
    #Check if we properly create the grid:
    #   Tpal1 verification:
    assert( len(grid.Tpal1) == 4 )
    print(" Tpal1  ==> {}".format(grid.Tpal2))
    assert( cmp(grid.Tpal1[0], [p1, p6]) )
    assert( cmp(grid.Tpal1[1], [p3]) )
    assert( cmp(grid.Tpal1[2], [p2, p4, p7]) )
    assert( cmp(grid.Tpal1[3], [p5]) )
    
    #   Tpal2 verifivation:
    assert( len(grid.Tpal2) == 3 )
    print(" Tpal2 ==> {}".format(grid.Tpal1))
    assert( cmp(grid.Tpal2[0], [p1, p2]) )
    assert( cmp(grid.Tpal2[1], [p3, p4, p5]) )
    assert( cmp(grid.Tpal2[2], [p6, p7]) )
    
    #Check the creation of Si for i in (1..4)
    assert(True)
    assert(True)
    assert(True)
    assert(True)

if __name__ == '__main__':
	main()
