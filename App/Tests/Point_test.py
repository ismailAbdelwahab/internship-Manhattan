#!/usr/bin/env python3
from Data_structs.Point import Point
from Data_structs.SetT import SetT

def main():
    ######## Starting tests for Point class #######
    # Creating  points ( Point() )
    p1 = Point(3,2)
    p2 = Point(10,7)
    p3 = Point(5,1)
   
    # String printing  ( str() )
    assert( str(p1) == "(3,2)" )
    assert( str(p2) == "(10,7)" )

    # Point compairaison ( == )
    assert( p1 != p2 )
    assert( p1 == Point(3,2) )
   
    # Metrics ( l1 )
    assert( p1.l1DistTo(p2) == 12 )
    assert( p1.l1DistTo(p3) == 3  )
    assert( p1.l1DistTo(p2) == p2.l1DistTo(p1) )
    assert( p1.l1DistTo(p1) == 0 )
    
    #Creation of sets
    lozengeSet = SetT()
    left = Point(0,1)
    top = Point(1,4)
    middle = Point(1,1)
    bot = Point(1,-1)
    right = Point(4,1)
    lozengeSet.addPoint(left)
    lozengeSet.addPoint(top)
    lozengeSet.addPoint(middle)
    lozengeSet.addPoint(bot)
    lozengeSet.addPoint(right)
    # Dominance ( isDominating )
    # No point can be dominated in our case:
    assert( not middle.isDominating(right,lozengeSet) )
    assert( not right.isDominating(left,lozengeSet) )
    assert( not right.isDominating(left,lozengeSet) )
    assert( not left.isDominating(right,lozengeSet) )
    # Efficience ( isEfficient )   #TODO: implement that
    assert( middle.isEfficient(lozengeSet) )
    # Equivalence ( isEquivalentTo ) #TODO: implement that

if __name__ == '__main__':
    main()
