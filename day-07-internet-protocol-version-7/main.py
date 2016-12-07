# takes input of one string and defines whether it contains abba or not
def contains_abba(input):
    for a in range(len(input) - 3):
        chunk = input[a:a+4]
        if chunk[0] == chunk[3] and chunk[1] == chunk[2] and chunk[0] != chunk[1]:
            return True
    return False

