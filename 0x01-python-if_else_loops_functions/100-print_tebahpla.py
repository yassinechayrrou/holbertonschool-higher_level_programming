#!/usr/bin/python3
i = 90
while i > 64:
    print("{:c}".format((i + 32) if not i % 2 else i), end="")
    i = i - 1
