#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 96 < ord(i) < 123:
            upper = chr(ord(i) - 32)
        else:
            upper = i
        print(upper, end="")
    print("")
