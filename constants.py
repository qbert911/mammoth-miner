
tilelist = [("wall",  "white", 0xE108),
            ("dirt0", "white", 0xE000),
            ("dirt1", "white", 0xE001),
            ("dirt2", "white", 0xE002),
            ("dirt3", "white", 0xE003),
            ("dirt4", "white", 0xE004),
            ("dirt9", "gray", 0xE004),
            ("find1", "white", 0xE020),
            ("player","white", 0xE400)
           ]
#------------------------------------------------------------------------------#
MESSAGE_SIZE_Y = 3
STATS_PANEL_X = 10
CELLS_ACROSS = 40
CELLS_DOWN = 20

SCALE = 2

FONT_SIZE_X = 8
FONT_SIZE_Y = 16
XFACTOR = int(FONT_SIZE_Y / FONT_SIZE_X)

CONSOLE_SIZE_X = CELLS_ACROSS * XFACTOR
CONSOLE_SIZE_Y = CELLS_DOWN

VIEWPORT_SIZE_X = int((CONSOLE_SIZE_X - STATS_PANEL_X - XFACTOR) / XFACTOR)
VIEWPORT_SIZE_Y = CONSOLE_SIZE_Y - MESSAGE_SIZE_Y

MAP_SIZE_X = VIEWPORT_SIZE_X
MAP_SIZE_Y = VIEWPORT_SIZE_Y
