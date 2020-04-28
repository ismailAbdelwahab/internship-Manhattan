#!/usr/bin/env python3

class SetT():
    def __init__(self):
        self.set = []
        self.nbPoints = 0
######################### Manage points ##############################
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
    def sortByX(self):
        self.set.sort( key = lambda point : point.x)
    def sortByY(self):
        self.set.sort( key = lambda point : point.y)
####################### Copy + str + repr ############################
    def copy(self):
        copy = SetT()
        for point in self.set:
            copy.addPoint( point )
        return copy

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
