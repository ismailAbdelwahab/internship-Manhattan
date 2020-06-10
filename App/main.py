#!/usr/bin/env python3
from sys import argv, exit 

from ErrorHandlers.ErrorHandler import throwError
from ErrorHandlers.ArgumentLineHandler import checkArgumentLine
from Parser.CSVParser import CSVParser

from Data_structs.Point import Point
from Data_structs.SetT import SetT
from Data_structs.GridT import GridT
from Data_structs.ParetoEnv import ParetoEnv
from Data_structs.OiAi import OiAi
######################## Main #######################################
def main():
    print("\t[1] Extracting data from CSV file:" )
    try:
        filename = argv[1] #"Ressources/csv_points/set1.csv"
        terms = CSVParser.createSetTFromFile( filename )
    except FileNotFoundError:
        throwError("The specified file does not exist.", 3, False) 
    print( "Terminals:" + str(terms) )

    print("\n========== Part 1: Pareto envelope ==========")
    print( "\t[2] Converting into unit coordinates:" )
    gridT = GridT( terms )
    correspondanceTable = gridT.correspondanceTable
    print( "Correspondance table \{Real point coordinates : unit coordinates\}:" )
    print( str(correspondanceTable) )

    print( "\n\t[3] Constructing Pareto envelope:" )
    pareto = ParetoEnv( terms )
    pareto.constructParetoEnv()
    print( "Printing Pareto envelope:" )
    print( str(pareto.paretoEnv) )

    print("\n======= Part 2: Strips and Staircases =======")
    print("\t[4] Computing Oi and Ai | For i in [1..4]:")
    oiAi = OiAi( terms )
    oiAi.computeDictionaries()
    print("O1 : " + str(oiAi.O1) )
    print("O2 : " + str(oiAi.O2) )
    print("O3 : " + str(oiAi.O3) )
    print("O4 : " + str(oiAi.O4) )
    print(" ------------- ")
    print("A1 : " + str(oiAi.A1) )
    print("A2 : " + str(oiAi.A2) )
    print("A3 : " + str(oiAi.A3) )
    print("A4 : " + str(oiAi.A4) )

if __name__ == '__main__':
    checkArgumentLine()
    main()


# Error codes:
#  1 => No file specified in command line
#  2 => Too much arguments/file given in command line
#  3 => File not found exception
