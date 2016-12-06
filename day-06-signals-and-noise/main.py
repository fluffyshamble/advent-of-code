import collections as c

# read in signals
# TODO: Re-order input to be a list of the columns i.e. [1111, 2222, 3333] rather than a raw list of the strings
def find_input(filename):
    text_file = open(filename, "r")
    output = text_file.read().split('\n')
    text_file.close()
    return zip(*output)


signals = find_input("signal.txt")
message = ""

# Part One
for signal in signals:
    message = message + c.Counter(signal).most_common()[0][0]

print message