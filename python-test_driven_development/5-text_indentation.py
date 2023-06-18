#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters(. ? :)"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        line = ""
        for char in text:
            line += char
            if (char == ".") or (char == "?") or (char == ":"):
                print(line.strip())
                print()
                line = ""
        if line:
            print(line.strip(), end="")
