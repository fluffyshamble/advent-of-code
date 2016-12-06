import collections as c


def solve_part_one(filename):
    text_file = open(filename, "r")
    output = text_file.read().split('\n')
    message = ""
    text_file.close()
    signals = zip(*output)
    for signal in signals:
        message = message + c.Counter(signal).most_common()[0][0]
    print "Message One: %s" % message
    return


def solve_part_two(filename):
    text_file = open(filename, "r")
    output = text_file.read().split('\n')
    message = ""
    text_file.close()
    signals = zip(*output)
    for signal in signals:
        message = message + c.Counter(signal).most_common()[-1][0]
    print "Message Two: %s" % message
    return


if __name__ == '__main__':
    solve_part_one("signal.txt")
    solve_part_two("signal.txt")