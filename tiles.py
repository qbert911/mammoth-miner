from bearlibterminal import terminal
import constants

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
    for x in range(len(constants.tilelist)):
        if constants.tilelist[x][0] == wor:
            return constants.tilelist[x][2]

def seek_tile_color(wor):
    for x in range(len(constants.tilelist)):
        if constants.tilelist[x][0] == wor:
            return constants.tilelist[x][1]
