#!/usr/bin/python3
def uppercase(str):
    convert = list(str)
    for c in range(len(convert)):
        if (ord(convert[i]) > 96 and ord(convert[i]) < 123):
            convert[i] = chr(ord(convert[i]) - 32)
            print("{:s}".format(convert[i]), end="")
    print("")
