"""
This code starts a new world and runs the main loop, waiting for each keypress
    Code organization is as follows:
        Mainloop -> runs a World -> contains a Map
        - Main handles keypresses and timing
        - World handles Tiles and drawing and player actions
        - Maps handles coordinates and stores data
"""
# pylint: disable=C0103,C0301
import time
from bearlibterminal import terminal
import constants
import world

def mainLoop():
    w = world.World()
    w.draw_screen()
    key = None
    while key not in (terminal.TK_CLOSE, terminal.TK_ESCAPE):
        key = terminal.read()
        if key in (terminal.TK_ESCAPE, terminal.TK_CLOSE):
            break
        if key in constants.MOVE_keys:
            w.try_move(key)
        elif key == terminal.TK_KP_PLUS:
            constants.SCALE += 1
            w.log.append("Zoomed in - scale set to: "+str(constants.SCALE))
            w.dirty_tiles = True
            terminal.set("font: tiles/VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
            terminal.set("font: tiles/VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
        elif key == terminal.TK_KP_MINUS:
            constants.SCALE -= 1
            w.log.append("Zoomed out - scale set to: "+str(constants.SCALE))
            w.dirty_tiles = True
            terminal.set("font: tiles/VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
        else:
            pass #ignore input
    #do game world processing between turns
        for a in range(constants.TICKS_PER_ACTION):
            w.log[-1] += ("tick "+str(a+1))
            w.do_gravity_stuff()
            w.draw_screen()
            time.sleep(constants.DELAY_PER_TICK/1000)



if __name__ == "__main__":
    terminal.open()
    #TODO:  figure out how to load constants settings from an ini file
    terminal.set("window: size="+str(constants.CONSOLE_SIZE_X)+"x"+str(constants.CONSOLE_SIZE_Y)+
                 ", title='FLUID SIMULATION'; font: tiles/VeraMono.ttf, size="+
                 str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.composition(True)
    mainLoop()
    terminal.close()
