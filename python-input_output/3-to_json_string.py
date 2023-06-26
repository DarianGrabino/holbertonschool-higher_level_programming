#!/usr/bin/python3
"""Write a function that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object(codificacion)"""
    return json.dumps(my_obj)
