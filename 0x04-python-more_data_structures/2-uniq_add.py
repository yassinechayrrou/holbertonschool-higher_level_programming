#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for s in set(my_list):
        res += s
    return res
