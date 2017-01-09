import time

import asciimatics.screen

from cryOSHardware import cryOSHardwareSet

__version__ = 0.2


def main(cryOS_main):
    cryOS_main.clear()

    cryophor0_1 = cryOSHardwareSet()
    # TODO: declare temp sensors

    # Title
    cryOS_main.print_at("cryOS v" + str(__version__), 0, 0)

    # Draw diagram of apparatus
    # TODO: investigate using diagram as triple-quoted string, then splitlines(). Cleaner?
    for line_number, text in enumerate(cryophor0_1.diagram):
        cryOS_main.print_at(text, line_number + 2, 10)

    # TODO: draw temp sensors

    cryOS_main.refresh()
    time.sleep(5)


if __name__ == '__main__':
    # Prepare window with wrapper that takes care of resetting Terminal settings
    asciimatics.screen.Screen.wrapper(main)
