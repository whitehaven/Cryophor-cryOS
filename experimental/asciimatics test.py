import asciimatics.screen


def demo(screen):
    screen.print_at('Hello world!', 0, 0)


asciimatics.screen.Screen.wrapper(demo)
