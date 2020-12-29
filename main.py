from bearlibterminal import terminal
import load
import constants
import world

# pylint: disable=C0103,C0301

def mainLoop():
    w = world.world()

    key = None
    while key not in (terminal.TK_CLOSE, terminal.TK_ESCAPE):
        w.draw_screen()
        key = terminal.read()
        if key in (terminal.TK_ESCAPE, terminal.TK_CLOSE):
            break
        if key == terminal.TK_DOWN:
            sti ="down"
        elif key == terminal.TK_UP:
            sti ="up"
        elif key == terminal.TK_LEFT:
            sti ="left"
        elif key == terminal.TK_RIGHT:
            sti ="right"
        elif key == terminal.TK_KP_PLUS:
            constants.SCALE += 1
            sti = "Scale set to: "+str(constants.SCALE)
            load.tiles()
            terminal.set("font: VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
            terminal.set("font: VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
        elif key == terminal.TK_KP_MINUS:
            constants.SCALE -= 1
            sti = "Scale set to: "+str(constants.SCALE)
            load.tiles()
            terminal.set("font: VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
        else:
            sti = "unknown"

        w.log.append(sti)


if __name__ == "__main__":
    terminal.open()
    terminal.set("window: size="+str(constants.CONSOLE_SIZE_X)+"x"+str(constants.CONSOLE_SIZE_Y)+", title='mm test'; font: VeraMono.ttf, size="+str(constants.FONT_SIZE_X*constants.SCALE)+"x"+str(constants.FONT_SIZE_Y*constants.SCALE))
    terminal.composition(True)
    terminal.color("white")
    load.tiles()
    mainLoop()
    terminal.set("U+E200: none")
    terminal.composition(False)
    terminal.close()
