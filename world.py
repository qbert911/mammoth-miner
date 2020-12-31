"""
This code defines the world class which handles the interaction
    between player and map elements
"""
# pylint: disable=C0103,C0301
import random
from bearlibterminal import terminal
import constants
import tiles
import maps

class World:
    def __init__(self):
        self.this_map = maps.Map()
        self.dirty_tiles = True
        self.log = ['']*constants.MESSAGE_SIZE_Y
        self.player_score = 0
        self.view_offset_x = 0
        self.view_offset_y = 0
        self.player_x = int(random.random()*constants.MAP_SIZE_X)
        self.player_y = constants.MAP_SIZE_Y - 1

        self.startup_menu()
        self.log.append("Let's get mining...")

    def do_gravity_stuff(self):
        pass

    def startup_menu(self):
        pass

#   def load_game(self):
#   def save_game(self):
#   def reset_game(self):

    def draw_screen(self):
        if self.dirty_tiles:
            tiles.load_tiles()
            self.log.append("tiles loaded")
            self.dirty_tiles = False
        terminal.clear()
#Draw message log
        for m in range(constants.MESSAGE_SIZE_Y+1):
            terminal.puts(0, constants.CONSOLE_SIZE_Y-m, self.log[-m])
#Draw side info panel
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 0, "Score:"+str(self.player_score))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 1, "x:"+str(self.player_x)+" y:"+str(self.player_y))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 3, "+/- scale:"+str(constants.SCALE))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 6, "o/p tick:"+str(constants.TICKS_PER_ACTION))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 7, "k/l delay:"+str(constants.DELAY_PER_TICK))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 15, "view:"+str(constants.MAP_SIZE_X)+"x"+str(constants.MAP_SIZE_Y))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 16, "win:"+str(constants.CELLS_ACROSS)+"x"+str(constants.CELLS_DOWN))
#Draw border
        for y in range(constants.CONSOLE_SIZE_Y):
            terminal.color(tiles.seek_tile_color("wall")) #unneeded
            terminal.put(int(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X-constants.XFACTOR), y, tiles.seek_tile("wall"))
#draw each tile background
        for x in range(int(constants.VIEWPORT_SIZE_X)):
            for y in range(constants.VIEWPORT_SIZE_Y):
                mytile = "dirt"+str(self.this_map.map_cosmetic_bg[x+self.view_offset_x][y+self.view_offset_y])
                terminal.color(tiles.seek_tile_color(mytile))
                terminal.put(x*constants.XFACTOR, y, tiles.seek_tile(mytile))
#draw text on top if desired
                if self.this_map.mapdata[x+self.view_offset_x][y+self.view_offset_y] > 0:
                    myout = "" #self.this_map.mapdata[x+self.view_offset_x][y+self.view_offset_y]
                    #myout = self.this_map.map_cosmetic_bg[x+self.view_offset_x][y+self.view_offset_y] #for testing
                else:
                    myout = ""
                terminal.puts(x*constants.XFACTOR, y, str(myout).rjust(2))
#draw each foreground symbol on top of background
                if self.this_map.map_cosmetic_fg[x+self.view_offset_x][y+self.view_offset_y] > 0:
                    mytile = "find"+str(self.this_map.map_cosmetic_fg[x+self.view_offset_x][y+self.view_offset_y])
                    terminal.color(tiles.seek_tile_color(mytile))
                    terminal.put(x*constants.XFACTOR, y, tiles.seek_tile(mytile))
#Draw player sprite last
        terminal.color(tiles.seek_tile_color("player"))
        terminal.put(self.player_x*constants.XFACTOR, self.player_y, tiles.seek_tile("player"))
        terminal.refresh()

    def try_move(self, inputkey):
        if inputkey == terminal.TK_DOWN:
            dx =  0;  dy = +1
        elif inputkey == terminal.TK_UP:
            dx =  0;  dy = -1
        elif inputkey == terminal.TK_LEFT:
            dx = -1;  dy = 0
        elif inputkey == terminal.TK_RIGHT:
            dx = +1;  dy = 0

        if  maps.is_in_bounds(self.player_x+dx,self.player_y+dy):
            #self.log.append("Moved "+ str(dx)+" "+str(dy))
            self.player_x += dx
            self.player_y += dy
            self.action_player_enters_square()
        else:
            self.log.append("Blocked "+ str(dx)+" "+str(dy))

    def action_player_enters_square(self):
        self.this_map.examine_surroundings(self.player_x,self.player_y)
        if self.this_map.mapdata[self.player_x][self.player_y] == 1:
            self.player_score += 1
            self.log.append("Found a rock")
        else:
            self.log.append("")
        self.this_map.hollow_square(self.player_x,self.player_y)
