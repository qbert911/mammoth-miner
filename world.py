from bearlibterminal import terminal
import random
import constants

class world:
    def __init__(self):
        self.data = []
        self.log = ['']*constants.MESSAGE_SIZE_Y
        self.mapdata = [[int(random.random()*2) for i in range(constants.MAP_SIZE_Y)]
                                                for j in range(constants.MAP_SIZE_X)]
        self.map_cosmetic_bg = [[int(random.random()*5) for i in range(constants.MAP_SIZE_Y)]
                                                for j in range(constants.MAP_SIZE_X)]
    def draw_screen(self):
        terminal.clear()
        #draw border
        for y in range(constants.CONSOLE_SIZE_Y):
            terminal.put(int(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X), y, 0xE200+8)
        #draw map
        for x in range(int(constants.MAP_SIZE_X)):
            for y in range(constants.MAP_SIZE_Y):
                #draw each tile background
                terminal.put(x*constants.XFACTOR, y, 0xE000+self.map_cosmetic_bg[x][y])
                #draw each symbol on top of background
                #terminal.put(x*constants.XFACTOR, y, 0xE000+self.mapcosmetic[x][y])
                #draw text on top
                if self.mapdata[x][y] > 0:
                    myout = self.mapdata[x][y]
                else:
                    myout = ""
                terminal.puts(x*constants.XFACTOR, y, str(myout).rjust(2))
        #draw message log
        for m in range(constants.MESSAGE_SIZE_Y+1):
            #terminal.puts(0, constants.CONSOLE_SIZE_Y-2, self.log[-2])
            terminal.puts(0, constants.CONSOLE_SIZE_Y-m, self.log[-m])
        #draw info panel
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X+constants.XFACTOR, 0, "Info line1")
        terminal.puts(constants.CONSOLE_SIZE_X-constants.STATS_PANEL_X+constants.XFACTOR, 1, "Info line2")

        terminal.refresh()
