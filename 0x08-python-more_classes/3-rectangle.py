#!/usr/bin/python3
"""
Rectangle module.
This module provides a rectangle class.
"""


class Rectangle:
    """Rectangle class with attributes and methods.
    Attributes : height and width.
    methods: area, perimeter and str.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self, value):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """method that returns area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """method that returns perimeter of rectangle"""
        h = self.__height
        w = self.__width
        return 0 if h is 0 or w is 0 else (h + w) * 2

    def __str__(self):
        """method that returns printable rectangle"""
        printrec = ""
        if self.__height is 0 or self.__width is 0:
            return printrec
        for i in range(self.__height):
            printrec += ("#" * self.__width)
            printrec += "\n"
        return printrec[:-1]
