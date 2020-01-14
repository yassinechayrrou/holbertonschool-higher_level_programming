#!/usr/bin/python3
"""
This is the "add_integer" module.
This module contain one function, add_integer(a, b).

The function adds a and b of type int or float and returns an int.
"""


def add_integer(a, b=98):
    """add_integer sums a and b.
    Return an integer as Result.
    Raise TypeError in case a or b is not float or int."""
    if (isinstance(a, int) or isinstance(a, float)) is False:
        raise TypeError("a must be an integer")
    elif (isinstance(b, int) or isinstance(b, float)) is False:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
