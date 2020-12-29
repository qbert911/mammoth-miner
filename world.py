"""
This code defines the world class and all the interaction between elements
"""
# pylint: disable=C0103,C0301
from bearlibterminal import terminal
import random
import constants
import tiles

class World:
    def __init__(self):
        self.log = ['']*constants.MESSAGE_SIZE_Y
        self.log.append("Let's get mining...")
        self.view_offset_x = 0
        self.view_offset_y = 0
        self.player_x = 10
        self.player_y = 10
        self.player_score = 0
        self.mapdata = [[int(random.random()*1.1) for i in range(constants.MAP_SIZE_Y)]
                                                for j in range(constants.MAP_SIZE_X)]
        self.map_cosmetic_bg = [[int(random.random()*8) for i in range(constants.MAP_SIZE_Y)]
                                                        for j in range(constants.MAP_SIZE_X)]
        self.map_cosmetic_fg = [[int(0) for i in range(constants.MAP_SIZE_Y)]
                                        for j in range(constants.MAP_SIZE_X)]
        self.startup_menu()

    def startup_menu(self):
        pass

#   def load_game(self):
#   def save_game(self):
#   def reset_game(self):

    def draw_screen(self):
        terminal.clear()
        for x in range(int(constants.VIEWPORT_SIZE_X)):
            for y in range(constants.VIEWPORT_SIZE_Y):
#draw each tile background
                mytile = "dirt"+str(self.map_cosmetic_bg[x+self.view_offset_x][y+self.view_offset_y])
                terminal.color(tiles.seek_tile_color(mytile))
                terminal.put(x*constants.XFACTOR, y, tiles.seek_tile(mytile))
#draw text on top if desired
                if self.mapdata[x+self.view_offset_x][y+self.view_offset_y] > 0:
                    myout = "" #self.mapdata[x+self.view_offset_x][y+self.view_offset_y]
                    #myout = self.map_cosmetic_bg[x+self.view_offset_x][y+self.view_offset_y] #for testing
                else:
                    myout = ""
                terminal.puts(x*constants.XFACTOR, y, str(myout).rjust(2))
#draw each foreground symbol on top of background
                if self.map_cosmetic_fg[x+self.view_offset_x][y+self.view_offset_y] > 0:
                    mytile = "find"+str(self.map_cosmetic_fg[x+self.view_offset_x][y+self.view_offset_y])
                    terminal.color(tiles.seek_tile_color(mytile))
                    terminal.put(x*constants.XFACTOR, y, tiles.seek_tile(mytile))
#Draw player sprite
        terminal.color(tiles.seek_tile_color("player"))
        terminal.put(self.player_x*constants.XFACTOR, self.player_y, tiles.seek_tile("player"))
#Draw border
        for y in range(constants.CONSOLE_SIZE_Y):
            terminal.color(tiles.seek_tile_color("wall")) #unneeded
            terminal.put(int(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X-constants.XFACTOR), y, tiles.seek_tile("wall"))
#Draw message log
        for m in range(constants.MESSAGE_SIZE_Y+1):
            terminal.puts(0, constants.CONSOLE_SIZE_Y-m, self.log[-m])
#Draw info panel
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 0, "Score:")
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 1, str(self.player_score))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 4, str(self.player_x)+" "+str(self.player_y))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 10, "view "+str(constants.MAP_SIZE_X)+" "+str(constants.MAP_SIZE_Y))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 11, str(constants.STATS_PANEL_X)+"(/"+str(constants.XFACTOR)+") "+str(constants.MESSAGE_SIZE_Y))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 14, str(constants.CELLS_ACROSS)+" "+str(constants.CELLS_DOWN))
        terminal.refresh()

    def is_in_bounds(self,xin,yin):
        if xin+self.player_x >= constants.MAP_SIZE_X or xin+self.player_x < 0 or \
           yin+self.player_y >= constants.MAP_SIZE_Y or yin+self.player_y < 0:
            return False
        return True

    def try_move(self, inputkey):
        if inputkey == terminal.TK_DOWN:
            dx =  0;  dy = +1
        elif inputkey == terminal.TK_UP:
            dx =  0;  dy = -1
        elif inputkey == terminal.TK_LEFT:
            dx = -1;  dy = 0
        elif inputkey == terminal.TK_RIGHT:
            dx = +1;  dy = 0

        if self.is_in_bounds(dx,dy):
            #self.log.append("Moved "+ str(dx)+" "+str(dy))
            self.player_x += dx
            self.player_y += dy
            self.action_player_enters_square()
        else:
            self.log.append("Blocked "+ str(dx)+" "+str(dy))

    def action_player_enters_square(self):
        self.examine_surroundings()
        if self.mapdata[self.player_x][self.player_y] == 1:
            self.player_score += 1
            self.log.append("Found a rock")
        #else:
        #    self.log.append("Nothing here")
        self.mapdata[self.player_x][self.player_y] = 0
        self.map_cosmetic_fg[self.player_x][self.player_y] = 0
        self.map_cosmetic_bg[self.player_x][self.player_y] = 9


    def examine_cell(self, dx, dy):
        if self.is_in_bounds(dx, dy):
            if self.mapdata[self.player_x+dx][self.player_y+dy] > 0:
                self.map_cosmetic_fg[self.player_x+dx][self.player_y+dy] = 1

    def examine_surroundings(self):
        self.examine_cell(-1,-1)
        self.examine_cell(-1, 0)
        self.examine_cell(-1,+1)
        self.examine_cell( 0,-1)
        self.examine_cell( 0,+1)
        self.examine_cell(+1,-1)
        self.examine_cell(+1, 0)
        self.examine_cell(+1,+1)
