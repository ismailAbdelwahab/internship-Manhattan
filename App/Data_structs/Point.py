#!/usr/bin/env python3

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "Point:({},{})\n".format(self.x, self.y)

    def __str__(self):
        return "({},{})".format(self.x, self.y)
