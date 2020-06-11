#!/usr/bin/env python3
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

################## Dominance of the point ##########################
    def isDominating(self, other, setT):
        """ Return True if "self" is dominating "other" in "setT". """
        strict_dominance = False
        for point in setT.set:
            selfToPoint = self.l1DistTo(point) 
            otherToPoint = other.l1DistTo( point )
            if selfToPoint < otherToPoint :
                strict_dominance = True
                continue
            elif selfToPoint == otherToPoint:
                continue
            else:
                return False
        return strict_dominance
#################### Efficient point ###############################
    def isEfficient(self, setT):
        """ Return True if no point in setT is dominating self """
        for point in setT.set:
            if point == self:
               continue
            if point.isDominating( self, setT ):
                return False
        return True
#################### Equivalence of points #########################
    def isEquivalentTo(self, other, setT):
        """ Return True if self.d(p) == other.d(p) for all p in setT """
        if self == other:
            return True;
        for point in setT.set:
            if self.l1DistTo( point ) != other.l1DistTo( point ):
                return False
        return True
################## Distances calculation ###########################
    def l1DistTo(self, other ):
        """ Return the l1-metric distance to the point in argument. """
        return abs(self.x - other.x) + abs(self.y - other.y) 
################## Object comparaison ##############################    
    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
######################## str + repr ################################
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    def __repr__(self):
        return self.__str__()
######################## Hash ######################################
    def __hash__(self):
        return hash(repr(self))
