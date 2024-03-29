#!/usr/bin/python3
"""Define the start of the class"""
import json
import os


class Base:
    """First class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """defines a private class attribute"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to file"""
        if list_objs is None:
            dict_objs = []
        else:
            dict_objs = [lists.to_dictionary() for lists in list_objs]
        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dict_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        if not os.path.isfile(filename):
            return []
        with open(filename, mode='r', encoding='utf-8') as f:
            json_string = f.read()
            list_of_dict = cls.from_json_string(json_string)
            list_of_instances = []
            for n in list_of_dict:
                list_of_instances.append(cls.create(**n))
            return list_of_instances
