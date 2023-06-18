#!/usr/bin/python3
""""print square"""


def print_square(size):
    """print square with given size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    else:
        for n in range(size):
            for i in range(size):
                print("#", end="")
            print()
