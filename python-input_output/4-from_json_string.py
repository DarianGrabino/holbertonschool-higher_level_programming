#!/usr/bin/python3
"""Write a function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string (decodificacion)"""
    return json.loads(my_str)
