"""
This code starts a new world
"""
# pylint: disable=C0103,C0301
from bearlibterminal import terminal
import load
import constants
import world

mykeys = [ terminal.TK_DOWN, terminal.TK_UP, terminal.TK_LEFT, terminal.TK_RIGHT]

def mainLoop():
    w = world.World()
    key = None
    while key not in (terminal.TK_CLOSE, terminal.TK_ESCAPE):
        w.draw_screen()
        key = terminal.read()
        if key in (terminal.TK_ESCAPE, terminal.TK_CLOSE):
            break
        if key in mykeys:
            sti = "moved"+ str(key)
            w.log.append(sti)
        elif key == terminal.TK_KP_PLUS:
            constants.SCALE += 1
            sti = "Scale set to: "+str(constants.SCALE)
            w.log.append(sti)
            load.tiles()
            terminal.set("font: VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
            terminal.set("font: VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
        elif key == terminal.TK_KP_MINUS:
            constants.SCALE -= 1
            sti = "Scale set to: "+str(constants.SCALE)
            w.log.append(sti)
            load.tiles()
            terminal.set("font: VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
        else:
            pass #ignore input

if __name__ == "__main__":
    terminal.open()
    terminal.set("window: size="+str(constants.CONSOLE_SIZE_X)+"x"+str(constants.CONSOLE_SIZE_Y)+
                 ", title='mm .01'; font: VeraMono.ttf, size="+
                 str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.composition(True)
    load.tiles()
    mainLoop()
    terminal.set("U+E200: none")
    terminal.composition(False)
    terminal.close()
