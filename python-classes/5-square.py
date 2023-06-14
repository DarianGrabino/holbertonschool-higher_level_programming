#!/usr/bin/python3
"""Define a class"""


class Square:
    """Define a class Square"""
    def __init__(self, size=0):
        """Initialize the class"""
        self.__size = size

    def area(self):
        """Calculate the area"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
