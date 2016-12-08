def create_screen(width, height):
    screen = []
    for i in range(0, height):
        new_line = []
        for j in range(0, width):
            new_line.append(".")
        screen.append(new_line)
    return screen


def print_screen(screen):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in screen]))


def rect(width, height, screen):
    for row in range(0, height):
        for column in range(0, width):
            screen[row][column] = '#'

def rot_col(column, rotation, height, screen):
    column_to_change = [row[column] for row in screen]
    for j in range(0, height):
        screen[j][column] = column_to_change[(j - rotation) % height]


def rot_row(row, rotation, width, screen):
    row_to_change = [i for i in screen[row]]
    for i in range(0, width):
        screen[row][i] = row_to_change[(i - rotation) % width]


screen_width = 50
screen_height = 6

screen = create_screen(screen_width, screen_height)
rect(3,2,screen)
rot_row(1, 2, screen_width, screen)
print_screen(screen)


# TODO: Parse instructions function