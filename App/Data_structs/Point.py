#!/usr/bin/env python3

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
################## Object comparaison ##############################    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
######################## str + repr ################################
    def __repr__(self):
        return "Point:({},{})".format(self.x, self.y)

    def __str__(self):
        return "({},{})".format(self.x, self.y)
