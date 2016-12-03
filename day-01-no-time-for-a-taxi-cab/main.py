def parsedirection(filename):
    text_file = open(filename, "r")
    output = text_file.read().split(',')
    return output

input = "directions.txt"
directions = parsedirection(input)
print directions