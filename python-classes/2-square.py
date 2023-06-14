#!/usr/bin/python3
"""Define a class"""


class Square:
    """Define a class Square with attribute"""
    def __init__(self, size=0):
        """add exception"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
