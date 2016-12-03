def parse_direction(filename):
    text_file = open(filename, "r")
    output = text_file.read().split(',')
    return output


def move(direction):
    facing = 0
    pos = [0,0]
    if "L" in direction:
        facing -= 1
        facing = facing % 4
    elif "R" in direction:
        facing += 1
        facing = facing % 4
    if facing == 0:
        pos[1] +=1
    elif facing == 1:
        pos[0] += 1
    elif facing == 2:
        pos[1] -= 1
    elif facing == 3:
        pos[0] -= 1
    return pos



input = "directions.txt"
directions = parse_direction(input)


