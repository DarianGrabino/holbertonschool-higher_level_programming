#!/usr/bin/python3
""" class square """


class Square:
    """ Private instance attribute: size and position """
    def __init__(self, __size=0, __position=(0, 0)):
        self.__size = __size
        self.__position = __position

        if len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(self.__position[0])) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(self.__position[1])) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (self.__position[0] < 0 or self.__position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    """ area of a square """
    def area(self):
        area = self.__size * self.__size
        return area
    """ Print a squares wiht position """
    def my_print(self):
        x = 0
        y = 0
        if (self.__size == 0):
            print()
            return
        for p1 in range(self.__position[1]):
            print()
        for x in range(self.__size):
            for p0 in range(self.__position[0]):
                print(" ", end="")
            for y in range(self.__size - 1):
                print("#", end="")
            print("#")
    """ Devolver un atributo de propiedad """
    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position
    """ permite establecer o mutar el valor de un atributo en una clase """
    @size.setter
    def size(self, value):
        if (type(value)) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
