# read in signals
def find_input(filename):
    text_file = open(filename, "r")
    output = text_file.read().split('\n')
    text_file.close()
    return output

signals = find_input("signal.txt")

for signal in signals:
    #
