from bearlibterminal import terminal
import random
import constants

class world:
    def __init__(self):
        self.data = []
        self.log = ["",""]
        self.mapdata = [[int(random.random()*8) for i in range(constants.MAP_SIZE_Y)]
                                                 for j in range(constants.MAP_SIZE_X)]
        self.mapcosmetic = [[int(random.random()*5) for i in range(constants.MAP_SIZE_Y)]
                                                 for j in range(constants.MAP_SIZE_X)]
    def draw_screen(self):
        terminal.clear()
        #draw border
        for y in range(constants.MAP_SIZE_Y):
            terminal.put(int(constants.MAP_SIZE_X*constants.XFACTOR), y, 0xE200+8)
        #draw map
        for x in range(int(constants.MAP_SIZE_X)):
            for y in range(constants.MAP_SIZE_Y):
                terminal.put(x*constants.XFACTOR, y, 0xE000+self.mapcosmetic[x][y])
                terminal.puts(x*constants.XFACTOR, y, str(self.mapdata[x][y]).rjust(2))
        #draw message log
            terminal.puts(0, 28, self.log[-2])
            terminal.puts(0, 29, self.log[-1])
        #draw info panel
        terminal.puts(102, 0, "Info line1")
        terminal.puts(102, 1, "Info line2")
        terminal.puts(102, 2, "Info line3")

        terminal.refresh()
