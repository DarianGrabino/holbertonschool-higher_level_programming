#!/usr/bin/python3
"""function that checks if the object is an instance of the class/
or if the object is an instance of a class that inherited"""


def is_kind_of_class(obj, a_class):
    """returns True or False"""
    return isinstance(obj, a_class)
