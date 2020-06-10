#!/usr/bin/env python3
class SetT():
    def __init__(self):
        self.set = []
        self.nbPoints = 0
################### Add and Remove points ############################
    def addPoint(self, point):
        self.set.append( point )
        self.nbPoints += 1

    def removePoint(self, p):
        for point in self.set:
            if point == p:
                self.set.remove(point)
                self.nbPoints -= 1
                return
        print("Point "+str(p)+" not found in set, cannot remove it.")
########################### Sort set #################################
    # Initial possibilities to sort:
    def sortByX(self):
        self.set.sort( key = lambda point : point.x )
    def sortByY(self):
        self.set.sort( key = lambda point : point.y )
    def sortByDecX(self):
        self.set.sort( key = lambda point : point.x, reverse = True)
    def sortByDecY(self):
        self.set.sort( key = lambda point : point.y, reverse = True)
    # Sorting by X THEN by Y:
    def sortIncXIncY(self):
        self.sortByY(); self.sortByX()
    def sortIncXDecY(self):
        self.sortByDecY(); self.sortByX()
    def sortDecXIncY(self):
        self.sortByY(); self.sortByDecX()
    def sortDecXDecY(self):
        self.sortByDecY(); self.sortByDecX()
    # Sorting by Y THEN by X:
    def sortIncYIncX(self):
        self.sortByX(); self.sortByY()
    def sortIncYDecX(self):
        self.sortByDecX(); self.sortByY()
    def sortDecYIncX(self):
        self.sortByX(); self.sortByDecY()
    def sortDecYDecX(self):
        self.sortByDecX(); self.sortByDecY()
####################### Copy  ########################################
    def copy(self):
        copy = SetT()
        for point in self.set:
            copy.addPoint( point )
        return copy
#################### eq + repr + str ################################# 
    def __eq__(self, other):
        return self.set == other.set and self.nbPoints == other.nbPoints
    
    def __repr__(self):
        return "Set of terminals: len={0}".format( self.nbPoints )
    
    def __str__(self):
        if self.nbPoints == 0:
            return "[]"
        string = "["
        for point in self.set:
            string += str(point) + ", "
        return string[:-2] + "]"
