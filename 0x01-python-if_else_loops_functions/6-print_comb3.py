#!/usr/bin/python3
for n in range(9):
    for m in range(n + 1, 10):
        print("{:d}{:d}, ".format(n, m), end="")
print("{:d}{:d}".format(n + 1, m))
