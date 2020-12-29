from bearlibterminal import terminal
import random
import constants

class World:
    def __init__(self):
        self.log = ['']*constants.MESSAGE_SIZE_Y
        self.log.append("Let's get mining...")
        self.view_offset_x = 0
        self.view_offset_y = 0
        self.mapdata = [[int(random.random()*2) for i in range(constants.MAP_SIZE_Y)]
                                                for j in range(constants.MAP_SIZE_X)]
        self.map_cosmetic_bg = [[int(random.random()*4) for i in range(constants.MAP_SIZE_Y)]
                                                for j in range(constants.MAP_SIZE_X)]

        self.startup_menu()

    def startup_menu(self):
        pass

#   def load_game(self):
#   def save_game(self):
#   def reset_game(self):
    def seek_tile(self,wor):
        for x in range(len(constants.tilelist)):
            if constants.tilelist[x][0] == wor:
                return constants.tilelist[x][2]

    def seek_tile_color(self,wor):
        for x in range(len(constants.tilelist)):
            if constants.tilelist[x][0] == wor:
                return constants.tilelist[x][1]

    def draw_screen(self):
        terminal.clear()
#draw map
        for x in range(int(constants.VIEWPORT_SIZE_X)):
            for y in range(constants.VIEWPORT_SIZE_Y):
                #draw each tile background
                mytile = "dirt"+str(self.map_cosmetic_bg[x+self.view_offset_x][y+self.view_offset_y])
                terminal.color(self.seek_tile_color(mytile))
                terminal.put(x*constants.XFACTOR, y, self.seek_tile(mytile))
                #draw each symbol on top of background
                terminal.color("white")
                #terminal.put(x*constants.XFACTOR, y, 0xE000+self.mapcosmetic[x][y])
                #draw text on top
                if self.mapdata[x+self.view_offset_x][y+self.view_offset_y] > 0:
                    myout = self.mapdata[x+self.view_offset_x][y+self.view_offset_y]
                    myout = self.map_cosmetic_bg[x+self.view_offset_x][y+self.view_offset_y] #for testing
                else:
                    myout = ""
                terminal.puts(x*constants.XFACTOR, y, str(myout).rjust(2))
#Draw border
        for y in range(constants.CONSOLE_SIZE_Y):
            terminal.color(self.seek_tile_color("wall")) #unneeded
            terminal.put(int(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X-constants.XFACTOR), y, self.seek_tile("wall"))
#Draw message log
        for m in range(constants.MESSAGE_SIZE_Y+1):
            terminal.puts(0, constants.CONSOLE_SIZE_Y-m, self.log[-m])
#Draw info panel
        #terminal.color(self.seek_tile_color("dirt3"))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 0, "Info line1")
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 1, "Info line2")
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 2, "1234567890abcdefg")
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 10, "view "+str(constants.MAP_SIZE_X)+" "+str(constants.MAP_SIZE_Y))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 11, str(constants.STATS_PANEL_X)+"(/"+str(constants.XFACTOR)+") "+str(constants.MESSAGE_SIZE_Y))
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X, 14, str(constants.CELLS_ACROSS)+" "+str(constants.CELLS_DOWN))
        #terminal.puts(2, 2, "dirt"+str(self.map_cosmetic_bg[2+self.view_offset_x][2+self.view_offset_y])+"foo")

        terminal.refresh()

    def try_move(self, inputkey):
        pass
