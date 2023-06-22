#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
     """initialize by validating size"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        self.__width = size
        self.__height = size

    def area(self):
       """area of square"""
        return self.__width ** 2
