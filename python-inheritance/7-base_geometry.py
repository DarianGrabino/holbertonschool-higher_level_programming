#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """class with method"""

    def area(self):
        """area with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
