#!/usr/bin/env python3
from sys import argv, exit 

from ErrorHandlers.ArgumentLineHandler import checkArgumentLine
from Data_structs.Point import Point
from Data_structs.SetT import SetT
######################## Main #######################################
def main():
    print("******* Point tests *************")
    p1 = Point(3,2)
    p2 = Point(10,3)
    print("p1 is : " + str(p1))
    print("It's representation is:\n"+repr(p1))
    
    print("******* SetT tests *************")
    terms = SetT()
    terms.addPoint( p2 )
    terms.addPoint( p1 )
    terms.addPoint( Point(7,20) )
    terms.addPoint( Point(9,20) )
    terms.addPoint( Point(8,20) )
    terms.addPoint( Point(6,20) )
    print("My set is: " + str(terms))
    print("Here is it's representation: "+ repr(terms))
    
    print(" **********Copy*************")
    copySet = terms.copy()
    print("My COPY is: " + str(copySet))
    print("Here is it's representation: "+ repr(copySet))

    print(" **Remove(on copy)**")
    copySet.removePoint( p2 )
    print("p2 should be removed: copySet is: "+str(copySet))

    print(" **Sorting by X**")
    terms.sortByX()
    print("terms shoudl be sorted: by x "+ str(terms))
    print(" **Sorting by Y**")
    terms.sortByY()
    print("terms shoudl be sorted: by Y "+ str(terms))

# General plan for the main:
    # 1) Read csv file
    #   -> store points's data
    # 2) Compute data if needed
    # 3) Calculate Pareto envelope
    # 4) Strips and staircases
    # 5) Use algo from [5]
if __name__ == '__main__':
    checkArgumentLine()
    main()


# Error codes:
#  1 => No file specified in command line
#  2 => Too much arguments/file given in command line
