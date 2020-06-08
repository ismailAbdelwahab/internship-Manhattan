#!/usr/bin/env python3
from sys import argv, exit 

from ErrorHandlers.ErrorHandler import throwError
from ErrorHandlers.ArgumentLineHandler import checkArgumentLine
from Parser.CSVParser import CSVParser

from Data_structs.Point import Point
from Data_structs.SetT import SetT
from Data_structs.GridT import GridT
from Data_structs.ParetoEnv import ParetoEnv
######################## Main #######################################
def main():
    print("[1] Extracting data from CSV file:" )
    try:
        filename = argv[1] #"Ressources/csv_points/set1.csv"
        terms = CSVParser.createSetTFromFile( filename )
    except FileNotFoundError:
        throwError("The specified file does not exist.", 3, False) 
    print( "\tTerminals:" )
    print( "\t"+ str(terms) ) # ==> extracted SetT from CSV file

    print( "[2] Converting into unit coordinates:" )
    gridT = GridT( terms )
    correspondanceTable = gridT.correspondanceTable
    print( "\tCorrespondance table \{point : unit_coord\}:" )
    print( "\t" + str(correspondanceTable) )

    print( "[3] Constructing Pareto envelope:" )
    pareto = ParetoEnv( terms )
    pareto.constructParetoEnv()
    print( "\tPrinting Pareto envelope:" )
    print( "\t"+ str(pareto.paretoEnv) )

if __name__ == '__main__':
    checkArgumentLine()
    main()


# Error codes:
#  1 => No file specified in command line
#  2 => Too much arguments/file given in command line
#  3 => File not found exception
