import hashlib

def hashify(to_hash):
    hashed = hashlib.md5(to_hash).hexdigest()
    return hashed


def door_one(door_id):
    index = 0
    passcode = ""
    hashed_input = ""


    while len(passcode) < 8:
        to_hash = door_id + str(index)
        hashed_input = hashify(to_hash)
        if hashed_input[0:5] == "00000":
            passcode = passcode + hashed_input[5]
            print hashed_input
        index += 1

    print "DOOR ONE PASSCODE: %s" % passcode

def door_two(door_id):
    index = 0
    passcode = ['_',
                '_',
                '_',
                '_',
                '_',
                '_',
                '_',
                '_',]
    hashed_input = ""

    while "_" in passcode:
        to_hash = door_id + str(index)
        hashed_input = hashify(to_hash)
        if hashed_input[0:5] == "00000":
            try:
                pos = int(hashed_input[5])
                if passcode[pos] == '_':
                    passcode[pos] = hashed_input[6]
                    print hashed_input
            except ValueError:
                print "%s - INVALID HASH: Invalid position signifier" % hashed_input
            except IndexError:
                print "%s - INVALID HASH: Position signifier out of range" % hashed_input
        index += 1
    print "DOOR TWO PASSCODE %s" % ''.join(passcode)


door_one("reyedfim")
door_two("reyedfim")
