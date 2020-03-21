#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return str
    newstr = ""
    for i in range(len(str)):
        if i != n:
            newstr = newstr + str[i]
    return newstr
