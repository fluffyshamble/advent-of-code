def create_screen(width, height):
    screen = []
    new_line = []
    for i in range(0, height):
        for j in range(0, width):
            new_line.append(".")
        screen.append(new_line)
    return screen


screen = create_screen(6, 2)
print screen

# TODO: Get screen initialisation sorted
# TODO: Create functions for each instruction type
# TODO: Parse instructions function