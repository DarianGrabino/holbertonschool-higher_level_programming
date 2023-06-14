#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self._size = size

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
