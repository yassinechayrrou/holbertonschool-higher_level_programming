#!/usr/bin/python3
"""Rectangle module for 0x0C-python project"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class with private instance attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.y = y
        self.x = x
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if (isinstance(val, int)) is False:
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if (isinstance(val, int)) is False:
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if (isinstance(val, int)) is False:
            raise TypeError("y must be an integer")
        elif val <= 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if (isinstance(val, int)) is False:
            raise TypeError("x must be an integer")
        elif val <= 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = val
