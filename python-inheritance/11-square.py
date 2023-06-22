#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """initialize by validating size"""
    def __init__(self, size):
        BaseGeometry.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(size, size)
        self.__width = size
        self.__height = size

    def area(self):
        """area of square"""
        return self.__width ** 2

    def __str__(self):
        print(f"[Square] {self.__width}/{self.__height}")
