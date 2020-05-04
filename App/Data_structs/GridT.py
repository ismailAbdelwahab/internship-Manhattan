#!/usr/bin/env python3
class GridT():
    def __init__(self):
        self.Tpal1 = []
        self.Tpal2 = []
        self.correspondanceTable = []

########### Create the grid ###################
    def computeGrid(self, terms):
        terms.sortByY()
        for point in terms.set:
            self.insertPointInTPal1( point )
            self.insertPointInTPal2( point )
        self.fillCorrespodanceTable()
        return self.correspondanceTable

    def insertPointInTPal1(self, point):
        """ Vertical lines in the grid """
        if len(self.Tpal1) == 0 :
            self.Tpal1.append( [point] ); return
        for i in range(0, len(self.Tpal1)):
            print("Tpal1 ==> " +str(self.Tpal1) )
            if self.Tpal1[i][0].x == point.x :
                self.Tpal1[i].append( point ); return
            elif point.x < self.Tpal1[i][0].x :
                self.Tpal1.insert(i+1, [point]); return
        self.Tpal1.insert(len(self.Tpal1), [point])

    def insertPointInTPal2(self, point):
        """ Horizontal lines in the grid """
        if len(self.Tpal2) == 0 :
            self.Tpal2.append( [point] ); return
        for i in range(0, len(self.Tpal2)):
            if self.Tpal2[i][0].y == point.y :
                self.Tpal2[i].append( point ); return
            elif point.y < self.Tpal2[i][0].y :
                self.Tpal2.insert(i+1, point); return
        self.Tpal2.insert(len(self.Tpal2), [point])

################## Correspondance table ##################
    def fillCorrespodanceTable(self):
        pass  #TODO: Fill correspondance table
