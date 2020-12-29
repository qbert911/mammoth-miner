"""
This code starts a new world and runs the main loop, waiting for each keypress
"""
# pylint: disable=C0103,C0301
from bearlibterminal import terminal
import tiles
import constants
import world

def mainLoop():
    w = world.World()
    key = None
    while key not in (terminal.TK_CLOSE, terminal.TK_ESCAPE):
        w.draw_screen()
        key = terminal.read()
        if key in (terminal.TK_ESCAPE, terminal.TK_CLOSE):
            break
        if key in constants.MOVE_keys:
            w.try_move(key)
        elif key == terminal.TK_KP_PLUS:
            constants.SCALE += 1
            w.log.append("Zoomed in - scale set to: "+str(constants.SCALE))
            tiles.load_tiles()
            terminal.set("font: VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
            terminal.set("font: VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
        elif key == terminal.TK_KP_MINUS:
            constants.SCALE -= 1
            w.log.append("Zoomed out - scale set to: "+str(constants.SCALE))
            tiles.load_tiles()
            terminal.set("font: VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
        else:
            pass #ignore input

if __name__ == "__main__":
    terminal.open()
    terminal.set("window: size="+str(constants.CONSOLE_SIZE_X)+"x"+str(constants.CONSOLE_SIZE_Y)+
                 ", title='mm .01'; font: VeraMono.ttf, size="+
                 str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.composition(True)
    tiles.load_tiles()
    mainLoop()
    terminal.close()
