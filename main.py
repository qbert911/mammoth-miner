from bearlibterminal import terminal
import load
import constants
import world

if __name__ == "__main__":
    terminal.open()
    terminal.set("window: size="+str(constants.CONSOLE_SIZE_X)+"x"+str(constants.CONSOLE_SIZE_Y)+", title='mm test'; font: VeraMono.ttf, size="+str(constants.FONT_SIZE_X)+"x"+str(constants.FONT_SIZE_Y))
    terminal.composition(True)
    terminal.color("white")

    load.tiles()
    world = world.world()
    world.draw_screen()

    key = None
    while key not in (terminal.TK_CLOSE, terminal.TK_ESCAPE):
        key = terminal.read()
        if key in (terminal.TK_ESCAPE, terminal.TK_CLOSE):
            break
        elif key == terminal.TK_DOWN:
            sti ="down"
        elif key == terminal.TK_UP:
            sti ="up"
        elif key == terminal.TK_LEFT:
            sti ="left"
        elif key == terminal.TK_RIGHT:
            sti ="right"

        world.log.append('moved'+sti)
        world.draw_screen()

    terminal.set("U+E200: none")
    terminal.composition(False)
    terminal.close()
