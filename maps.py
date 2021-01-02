"""
This code defines the Map class which is a series of 2D arrays

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
        self.earth = [[int(0) for i in range(constants.MAP_SIZE_Y)]
                             for j in range(constants.MAP_SIZE_X)]
        self.water = [[int(0) for i in range(constants.MAP_SIZE_Y)]
                              for j in range(constants.MAP_SIZE_X)]
        self.air = [[int(10) for i in range(constants.MAP_SIZE_Y)]
                          for j in range(constants.MAP_SIZE_X)]
        self.treasure = [[int(0) for i in range(constants.MAP_SIZE_Y)]
                            for j in range(constants.MAP_SIZE_X)]
        self.discovered = [[int(0) for i in range(constants.MAP_SIZE_Y)]
                                   for j in range(constants.MAP_SIZE_X)]
        self.random_background = [[int(random.random()*8) for i in range(constants.MAP_SIZE_Y)]
                                                          for j in range(constants.MAP_SIZE_X)]

    def miner_setup_map(self):
        self.treasure = [[int(random.random()*1.13) for i in range(constants.MAP_SIZE_Y)]
                                               for j in range(constants.MAP_SIZE_X)]
        for y in range(constants.MAP_SIZE_Y):
            for x in range(constants.MAP_SIZE_X):
                self.water[x][y] = int(random.random()*4)
                if y > 2 and x < constants.MAP_SIZE_X - 1:
                    self.earth[x][y] = 5
                self.airate(x,y)

    def hollow_square(self,x,y):
        self.treasure[x][y] = 0
        self.discovered[x][y] = 0
        self.random_background[x][y] = 9
        self.earth[x][y]=0
        self.airate(x,y)

    def examine_cell(self, dx, dy):
        if is_in_bounds(dx, dy):
            if self.treasure[dx][dy] > 0:
                self.discovered[dx][dy] = 1

    def examine_surroundings(self,x,y):
        self.examine_cell(-1+x,-1+y)
        self.examine_cell(-1+x, 0+y)
        self.examine_cell(-1+x,+1+y)
        self.examine_cell( 0+x,-1+y)
        self.examine_cell( 0+x,+1+y)
        self.examine_cell(+1+x,-1+y)
        self.examine_cell(+1+x, 0+y)
        self.examine_cell(+1+x,+1+y)

    def airate(self,x,y):
        self.air[x][y] = 10 - self.earth[x][y] - self.water[x][y]

    def do_gravity_stuff(self):
        for y in range(constants.MAP_SIZE_Y-1,0,-1):
            for x in range(constants.MAP_SIZE_X):
                if self.water[x][y-1] > 0 and self.air[x][y] > 0:
                    self.water[x][y] += 1
                    self.water[x][y-1] -= 1
                    self.airate(x,y)
                    self.airate(x,y-1)
