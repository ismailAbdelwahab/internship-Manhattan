#!/usr/bin/env python3
from Data_structs.Point import Point

def main():
    ######## Starting tests for Point class #######
    # Creating two points ( Point() )
    p1 = Point(3,2)
    p2 = Point(10,7)
    
    # String printing  ( str() )
    assert( str(p1) == "(3,2)" )
    assert( str(p2) == "(10,7)" )

    # Point compairaison ( == )
    assert( p1 != p2 )
    assert( p1 == Point(3,2) )
    
if __name__ == '__main__':
    main()
