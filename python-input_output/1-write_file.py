#!/usr/bin/python3
"""function that write a string to a text file"""


def write_file(filename="", text=""):
    """write a string to a text file (UTF8) and /
    returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
