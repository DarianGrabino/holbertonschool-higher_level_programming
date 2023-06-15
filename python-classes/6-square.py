#!/usr/bin/python3
"""Define a Class"""


class Square:
    """Define class Square"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size mus be >= 0")
        else:
            self.__size = size

        if (type(position) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(position[0]) != int) or (type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Calculate the area"""
        return (self.__size ** 2)

    def my_print(self):
        """Print Square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for y in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size mus be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int) or (type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
