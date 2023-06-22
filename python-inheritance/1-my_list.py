#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """that prints the list sorted"""
    def print_sorted(self):
        print(sorted(self))
