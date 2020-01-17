#!/usr/bin/python3
"""
Rectangle module.
This module provides a rectangle class.
"""


class Rectangle:
    """Rectangle class with attributes and methods.
    Attributes : height and width.
    methods: area, perimeter, print, str, repr, and del.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            printrec += str(self.print_symbol * self.__width)
            printrec += "\n"
        return printrec[:-1]

    def __repr__(self):
        """method that returns code needed to rebuild object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """object deletion method call"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """staticmethod that returns the biggest rectangle"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            return rect_1 if rect_1.area() >= rect_2.area() else rect_2
