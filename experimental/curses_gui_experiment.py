import curses

cryOS_main = curses.initscr()

cryOS_main.border(0)
cryOS_main.addstr(12, 25, "cryOS v0.1")

cryOS_main.getch()

curses.endwin()