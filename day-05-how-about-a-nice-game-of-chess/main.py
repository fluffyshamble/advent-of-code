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

    print "The passcode for Door One is %s" % passcode


door_one("reyedfim")
