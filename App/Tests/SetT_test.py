#!/usr/bin/env python3
from Data_structs.Point import Point
from Data_structs.SetT import SetT

def main():
    ############# Starting tests for SetT class ###############
    ##### Creating a set ( SetT() )
    terms = SetT()

    ##### Adding elements ( addPoint() )
    terms.addPoint( Point(3,2) )
    assert( str(terms) == "[(3,2)]" )
    terms.addPoint( Point(26,1) )
    terms.addPoint( Point(18,2) )
    terms.addPoint( Point(5,7) )
    assert( str(terms) == "[(3,2), (26,1), (18,2), (5,7)]" )
    assert( terms.nbPoints == 4 )

    ##### Removing elements ( removePoint() )
    terms.removePoint( Point(26,1) )
    assert( str(terms) == "[(3,2), (18,2), (5,7)]" )
    assert( terms.nbPoints == 3)
    # Unexisting point removed does not change anything.
    terms.removePoint( Point(1000,1000) )
    assert( str(terms) == "[(3,2), (18,2), (5,7)]" )
    assert( terms.nbPoints == 3)

    ##### Copy a SetT ( copy() )
    myCopy = terms.copy()
    assert( myCopy == terms )
    myCopy.removePoint( Point(3,2) )
    assert( myCopy != terms )

    ##### Sorting
    terms.addPoint( Point(2,2) )
    terms.addPoint( Point(27,9) )
    terms.addPoint( Point(36,2) )
    # Sort by X then by Y
    terms.sortByX()
    assert( str(terms) == "[(2,2), (3,2), (5,7), (18,2), (27,9), (36,2)]" )
    # Sort by Y then by X
    terms.sortByY()
    assert( str(terms) == "[(2,2), (3,2), (18,2), (36,2), (5,7), (27,9)]" )


if __name__ == '__main__':
    main()
