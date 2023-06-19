#!/usr/bin/python3
""" Class that define a rectangle"""


class Rectangle:
    """ Define a rectangle """
    __width = None
    __height = None

    """ Init """
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if width is None:
            width = 0
        else:
            self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if height is None:
            height = 0
        else:
            self.__height = height

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        width = self.__width
        heigth = self.__height
        if heigth is not None and width is not None:
            return width * heigth

    def perimeter(self):
        width = self.__width
        heigth = self.__height
        if heigth == 0 or width == 0:
            return 0
        elif heigth is not None and width is not None:
            return (width + heigth) * 2
