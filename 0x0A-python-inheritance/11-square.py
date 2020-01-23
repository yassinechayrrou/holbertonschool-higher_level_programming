#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""imports rectangle"""


class Square(Rectangle):
    """inherits everything from rectangle 9 with super"""
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
