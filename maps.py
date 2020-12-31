"""
This code defines the world class and all the interaction between elements
"""
# pylint: disable=C0103,C0301
import random
import constants

def is_in_bounds(xin,yin):
    if xin >= constants.MAP_SIZE_X or xin < 0 or \
       yin >= constants.MAP_SIZE_Y or yin < 0:
        return False
    return True

class Map:
    def __init__(self):
        self.mapdata = [[int(random.random()*1.13) for i in range(constants.MAP_SIZE_Y)]
                                                for j in range(constants.MAP_SIZE_X)]
        self.map_cosmetic_bg = [[int(random.random()*8) for i in range(constants.MAP_SIZE_Y)]
                                                        for j in range(constants.MAP_SIZE_X)]
        self.map_cosmetic_fg = [[int(0) for i in range(constants.MAP_SIZE_Y)]
                                        for j in range(constants.MAP_SIZE_X)]

    def hollow_square(self,x,y):
        self.mapdata[x][y] = 0
        self.map_cosmetic_fg[x][y] = 0
        self.map_cosmetic_bg[x][y] = 9

    def examine_cell(self, dx, dy):
        if is_in_bounds(dx, dy):
            if self.mapdata[dx][dy] > 0:
                self.map_cosmetic_fg[dx][dy] = 1

    def examine_surroundings(self,x,y):
        self.examine_cell(-1+x,-1+y)
        self.examine_cell(-1+x, 0+y)
        self.examine_cell(-1+x,+1+y)
        self.examine_cell( 0+x,-1+y)
        self.examine_cell( 0+x,+1+y)
        self.examine_cell(+1+x,-1+y)
        self.examine_cell(+1+x, 0+y)
        self.examine_cell(+1+x,+1+y)
