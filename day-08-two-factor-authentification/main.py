def create_screen(width, height):
    screen = []
    for i in range(0, height):
        new_line = []
        for j in range(0, width):
            new_line.append(".")
        screen.append(new_line)
    return screen


screen_width = 6
screen_height = 2

screen = create_screen(screen_width, screen_height)
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in screen]))


# TODO: Create functions for each instruction type
# TODO: Parse instructions function