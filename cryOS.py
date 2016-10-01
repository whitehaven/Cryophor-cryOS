import curses


def main(cryOS_main):
    cryOS_main.clear()
    choice_key = None
    while choice_key != 'q':
        cryOS_main.border()

        # TODO: Draw this
        """
      ||     ||  temp (at cooling element)
      ||     ||
      ||     ||
      ||     ||
      =========  temp (at cold side of Peltier element)
     +---------+ <- note that this is blue
     +---------+ <- this is red
      | | | | |  temp (at hot side of Peltier element)
        | | |
        | | |    ? temp (at heatsink)
          |
          |
        """
        cryOS_main.refresh()

        choice_key = cryOS_main.getkey()


if __name__ == '__main__':
    # Prepare window with wrapper that takes care of resetting Terminal settings
    curses.wrapper(main)
