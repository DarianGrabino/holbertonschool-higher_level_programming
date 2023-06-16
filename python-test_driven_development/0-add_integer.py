#!/usr/bin/python3
"""add integer"""


def add_integer(a, b=98):
    """ a + b"""
    try:
        result = int(a) + int(b)
    except TypeError:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if type(b) != int and type(b) != float:
            raise TypeError("b must be an integer")
    return result