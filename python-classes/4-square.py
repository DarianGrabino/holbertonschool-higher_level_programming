#!/usr/bin/python3
"""Define a class"""


class Square:
    """Define a class Square with attribute"""
    def __init__(self, size=0):
        self._size = size

    """calculate the area"""
    def area(self):
        return (self._size ** 2)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value
