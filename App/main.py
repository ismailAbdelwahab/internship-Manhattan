#!/usr/bin/env python3
from sys import argv, exit 

from ErrorHandlers.ErrorHandler import throwError
from ErrorHandlers.ArgumentLineHandler import checkArgumentLine

from Data_structs.Point import Point
from Data_structs.SetT import SetT
from Parser.CSVParser import CSVParser
######################## Main #######################################
def main():
    try:
        filename = argv[1] #"Ressources/csv_points/set1.csv"
        terms = CSVParser.createSetTFromFile( filename )
    except FileNotFoundError:
        throwError("The specified file does not exist.", 3, False) 

    print(terms) # ==> extracted SetT from CSV file


if __name__ == '__main__':
    checkArgumentLine()
    main()


# Error codes:
#  1 => No file specified in command line
#  2 => Too much arguments/file given in command line
#  3 => File not found exception
