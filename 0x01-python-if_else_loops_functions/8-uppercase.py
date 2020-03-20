#!/usr/bin/python3
def uppercase(str):
    i = ""
    for i in str:
        if 96 < ord(i) < 123:
            i = chr(ord(i) - 32)
        else:
            pass
        print(i, end="")
    print("")
