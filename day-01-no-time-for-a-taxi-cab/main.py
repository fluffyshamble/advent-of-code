def parse_direction(filename):
    text_file = open(filename, "r")
    output = text_file.read().split(',')
    return output


def move(direction, facing):
    if "L" in direction:
        facing -= 1
        facing = facing % 4
    elif "R" in direction:
        facing += 1
        facing = facing % 4





input = "directions.txt"
directions = parse_direction(input)

