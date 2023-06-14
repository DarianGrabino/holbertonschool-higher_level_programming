#!/usr/bin/python3
"""Define a class"""


class Square:
    """Define a class Square with attribute"""
    def __init__(self, size=0):
        self._size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """calculate the area"""
    def area(self):
        return (self._size ** 2)
