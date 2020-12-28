from bearlibterminal import terminal as blt
import load
import constants

def test_tilesets():
    # Load tilesets
    blt.composition(True)

    for x in range(int(constants.CONSOLE_SIZE_X/constants.XFACTOR)):
        for y in range(constants.CONSOLE_SIZE_Y):
            blt.put(x*constants.XFACTOR, y, 0xE200+y)

    blt.put((59)*constants.XFACTOR, 29, 0xE100+196)

    blt.puts(2, 10, "[color=orange]4.[/color] Like font characters, tiles may be freely colored and combined:")
    blt.put(2+2+0, 11, 0xE200+8)
    blt.color("lighter orange")
    blt.put(2+3+5, 11, 0xE200+8)
    blt.color("orange")
    blt.put(2+2+10, 11, 0xE200+8)
    blt.color("dark orange")
    blt.put(2+23+15, 11, 0xE200+8)

    blt.color("white")
    order = [11, 10, 18, 12, 13]
    for i in range(len(order)):
        blt.put(30 + i * 4, 11, 0xE200 + order[i]);
        blt.put(30 + (len(order)+1) * 4, 11, 0xE200 + order[i])

    blt.put(30 + len(order) * 4, 11, 0xE200 + 15)

    blt.refresh()

    key = None
    while key not in (blt.TK_CLOSE, blt.TK_ESCAPE):
        key = blt.read()

    # Clean up
    blt.set("U+E200: none")
    blt.composition(False)

if __name__ == "__main__":
    blt.open()
    blt.set("window: size="+str(constants.CONSOLE_SIZE_X)+"x"+str(constants.CONSOLE_SIZE_Y)+", title='mm test'; font: VeraMono.ttf, size="+str(constants.FONT_SIZE_X)+"x"+str(constants.FONT_SIZE_Y))
    blt.color("white")
    load.tiles()
    test_tilesets()
    blt.close()
