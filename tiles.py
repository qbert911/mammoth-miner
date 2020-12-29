"""
Loads tiles and provides lookup functions
"""
# pylint: disable=C0103,C0301,C0116
from bearlibterminal import terminal
import constants

tilelist = [("wall",  "white", 0xE108),     #wall for border
            ("dirt0", "white", 0xE000),
            ("dirt1", "white", 0xE001),
            ("dirt2", "white", 0xE002),
            ("dirt3", "white", 0xE003),
            ("dirt4", "white", 0xE004),
            ("dirt9", "gray",  0xE004),     #dark dirt
            ("find0", "white", 0xE125),     #blank tile
            ("find1", "white", 0xE020),     #rock overlay
            ("player","white", 0xE400)      #dwarf icon
           ]
#------------------------------------------------------------------------------#
def load_tiles():
    terminal.set("U+E000: tiles/Dirt1.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.set("U+E001: tiles/Dirt2.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.set("U+E002: tiles/Dirt3.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.set("U+E003: tiles/Dirt4.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.set("U+E004: tiles/Dirt5.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))

    terminal.set("U+E020: tiles/rock0.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))

    terminal.set("U+E400: tiles/dwarf.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))

    terminal.set("U+E100: tiles/Tiles.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.set("U+E200: tiles/trees_plants_rocks.png, size=32x32, align=top-left, resize="+str(constants.FONT_SIZE_Y*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))

def seek_tile(wor):
    for x in range(len(tilelist)):
        if tilelist[x][0] == wor:
            return tilelist[x][2]

def seek_tile_color(wor):
    for x in range(len(tilelist)):
        if tilelist[x][0] == wor:
            return tilelist[x][1]
