#!/usr/bin/env python3

from Data_structs.Point import Point
from Data_structs.SetT import SetT

class CSVParser():
    @staticmethod
    def getFileContent( filename ):
        """ Return every line of the file that does not
        start with a '#' """
        with open( filename, "r" ) as f:
            lines = f.read().splitlines()
        return [ line for line in lines if line[0]!='#' ]

    @staticmethod
    def createPoint( line ):
        """ Parse a string: "x,y" and create a point with
        those coordinates. """
        coords = line.split(',')
        return Point( coords[0], coords[1] )

    @staticmethod
    def createSetTFromFile( filename ):
        """ Create a SetT based on the content of filename """
        terms = SetT()
        for line in  CSVParser.getFileContent( filename ):
            terms.addPoint( CSVParser.createPoint(line) )
        return terms
