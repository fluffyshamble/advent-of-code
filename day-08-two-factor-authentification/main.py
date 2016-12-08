def read_file(filename):
    contents = open(filename, "r")
    output = contents.read().split('\n')
    return output

def create_screen(width, height):
    screen = []
    for i in range(0, height):
        new_line = []
        for j in range(0, width):
            new_line.append(" ")
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

def count_pixels(screen):
    pixels = 0
    for row in range(0, screen_height):
        for column in range(0, screen_width):
            if screen[row][column] == '#':
                pixels += 1
    return pixels


if __name__ == "__main__":
    screen_width = 50
    screen_height = 6
    cardswipe = read_file("cardswipe.txt")

    screen = create_screen(screen_width, screen_height)

    for line in cardswipe:
        if line.startswith("rect"):
            dim = line.split(" ")[1].split("x")
            rect(int(dim[0]), int(dim[1]), screen)

        elif line.startswith("rotate column"):
            translation = line.split(" ")
            column = int(translation[2][2:])
            rotation = int(translation[4])
            rot_col(column, rotation, screen_height, screen)

        elif line.startswith("rotate row"):
            translation = line.split(" ")
            row = int(translation[2][2:])
            rotation = int(translation[4])
            rot_row(row, rotation, screen_width, screen)

    print_screen(screen)
    print "Lit pixels = %d" % count_pixels(screen)