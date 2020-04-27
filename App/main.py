#!/usr/bin/env python3
from sys import argv, exit 

from ErrorHandlers.ArgumentLineHandler import checkArgumentLine
from Data_structs.Point import Point

######################## Main #######################################
def main():
    p1 = Point(3,2)
    print("p1 is : " + str(p1))
    print("It's representation is:\n"+repr(p1))
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
