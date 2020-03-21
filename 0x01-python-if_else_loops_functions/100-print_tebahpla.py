#!/usr/bin/python3
i = 90
while i > 64:
    if i % 2 == 0:
        k = chr(i+32)
    if i % 2 != 0:
        k = chr(i)
    print(k, end="")
    i = i-1
