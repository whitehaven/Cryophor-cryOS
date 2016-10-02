import curses
# TODO: investigate use of pygcurse terminal drawing. May have high overhead.
from cryOSHardware import cryOSHardwareSet

__version__ = 0.2

def main(cryOS_main):
    cryOS_main.clear()
    choice_key = None

    cryophor0_1 = cryOSHardwareSet()
    # TODO: declare temp sensors

    while choice_key != 'q':

        # Title
        cryOS_main.addstr(0, 0, "cryOS v" + str(__version__))

        # Draw diagram of apparatus
        # cryOS_main.border()
        # TODO: investigate using diagram as triple-quoted string, then splitlines(). Cleaner?
        for line_number, text in enumerate(cryophor0_1.diagram):
            cryOS_main.addstr(line_number + 2, 10, text)

        # TODO: draw temp sensors

        cryOS_main.refresh()

        choice_key = cryOS_main.getkey()

if __name__ == '__main__':
    # Prepare window with wrapper that takes care of resetting Terminal settings
    curses.wrapper(main)
