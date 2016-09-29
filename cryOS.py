import curses


def main(cryOS_main):
    cryOS_main.clear()

    # wait for keypress to finish
    cryOS_main.getkey()


if __name__ == '__main__':
    # Prepare window with wrapper that takes care of resetting Terminal settings
    curses.wrapper(main)
