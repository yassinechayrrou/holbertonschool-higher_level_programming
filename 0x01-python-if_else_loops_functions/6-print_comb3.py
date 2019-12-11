#!/usr/bin/python3
for n in range(9):
    for m in range(n + 1, 10):
        if n != 8 and m != 9:
                print("{:d}{:d}, ".format(n, m), end="")
print("{:d}{:d}".format(8, 9))
