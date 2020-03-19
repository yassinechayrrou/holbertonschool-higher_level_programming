#!/usr/bin/python3
for n in range(10):
    for m in range(10):
        if n != 8 and m != 9:
            if n != m and n < m:
                print("{:d}{:d}, ".format(n, m), end="")
print("89")
