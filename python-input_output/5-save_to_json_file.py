#!/usr/bin/python3
"""Write a function that writes an Object to a text file, using a JSON"""
import json


def save_to_json_file(my_obj, filename):
    """the json.dumps method to encode the my_obj object into a JSON/
        string. The encoded string is passed to the file.write"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
