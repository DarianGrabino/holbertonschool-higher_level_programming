#!/usr/bin/python3
"""check if it is an instance of the class or subclass"""


def inherits_from(obj, a_class):
    """first check if it is an instance of the class and then the subclass"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
