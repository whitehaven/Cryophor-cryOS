import curses


def main(cryOS_main):
    cryOS_main.clear()

    cryOS_main.addstr(10, 12, 'poooooos', curses.A_REVERSE)

    cryOS_main.getkey()


curses.wrapper(main)
