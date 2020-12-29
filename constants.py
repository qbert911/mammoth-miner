
tilelist = [("wall", "white", 0xE200+8),
            ("dirt0", "white", 0xE000+0),
            ("dirt1", "orange", 0xE000+2),
            ("dirt2", "green", 0xE000+3),
            ("dirt3", "gray", 0xE000+4),
            ("dirt4", "dark gray", 0xE000+5),
            ("rock", "white", 0xE100+1)
           ]
#------------------------------------------------------------------------------#
MESSAGE_SIZE_Y = 3
STATS_PANEL_X = 10
CELLS_ACROSS = 40
CELLS_DOWN = 24

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
