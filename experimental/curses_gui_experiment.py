import curses
import time

cryOS_main = curses.initscr()

cryOS_main.border(0)
cryOS_main.addstr(12, 25, "cryOS v0.1", curses.A_BLINK)
for i in range(100):
    cryOS_main.refresh()
    time.sleep(.1)
cryOS_main.getch()

curses.endwin()
