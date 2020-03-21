#!/usr/bin/python3
i = 90
while i > 64:
    print(chr(i) if i % 2 is not 0 else chr(i + 32), end="")
    i = i - 1
