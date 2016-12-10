def read_file(filename):
    contents = open(filename, "r")
    output = contents.read()
    return output

def decompress(filename):
    message = read_file(filename)
    length = len(message)
    print "length = %s" % length
    i = 0
    while i < length:
        if message[i] == '(':
            marker = ""
            i += 1
            while message[i] != ')':
                marker += message[i]
                i += 1
            print "marker = %s" % marker
        i += 1
    return


if __name__ == '__main__':
    decompress('test_compressed.txt')

