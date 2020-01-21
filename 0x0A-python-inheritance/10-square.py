#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""imports rectangle"""


class Square(Rectangle):
    """inherits everything from rectangle 9 with super"""
    def __init__(__self, size):
        super().__init__(size, size)
