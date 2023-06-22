#!/usr/bin/python3
"""function that checks if the object is an instance of the class"""


def is_same_class(obj, a_class):
    """returns True or False"""
    if type(obj) is a_class:
        return True
    else:
        return False
