"""
Loads tiles and provides lookup functions
"""
# pylint: disable=C0103,C0301,C0116
from bearlibterminal import terminal
import constants

tilelist = [("wall",  "white", 0xE100+8),       #wall for border
            ("dirt0", "dark white", 0xE100+19), #recolored sand tile from tiles.png
            ("dirt1", "gray", 0xE100+19),       #recolored sand tile from tiles.png
            ("dirt2", "dark gray", 0xE100+19),  #recolored sand tile from tiles.png
            ("dirt3", "white", 0xE000+0),
            ("dirt4", "white", 0xE000+1),
            ("dirt5", "white", 0xE000+2),
            ("dirt6", "white", 0xE000+3),
            ("dirt7", "white", 0xE000+4),
            ("dirt9", "gray",  0xE000+4),       #dark dirt for explored areas
            ("find0", "white", 0xE400+1348),    #blank tile
            ("find1", "white", 0xE400+1588),    #? overlay
            ("player","white", 0xE400+13)       #character
           ]
#------------------------------------------------------------------------------#
def load_tiles():
    terminal.set("U+E000: tiles/Dirt1.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.set("U+E001: tiles/Dirt2.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.set("U+E002: tiles/Dirt3.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.set("U+E003: tiles/Dirt4.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.set("U+E004: tiles/Dirt5.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))

    terminal.set("U+E020: tiles/rock0.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))

    terminal.set("U+E100: tiles/Tiles.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
#    terminal.set("U+E200: tiles/trees_plants_rocks.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.set("U+E400: tiles/rltiles-2d.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))

def seek_tile(wor):
    for x in range(len(tilelist)):
        if tilelist[x][0] == wor:
            return tilelist[x][2]

def seek_tile_color(wor):
    for x in range(len(tilelist)):
        if tilelist[x][0] == wor:
            return tilelist[x][1]
