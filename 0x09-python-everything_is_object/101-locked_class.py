#!/usr/bin/python3
"""LockedClass module"""


class LockedClass:
    """LockedClass a class that prevents any attributes other then assigned
    in __slots__"""

    __slots__ = ['first_name']
