#!/usr/bin/python3
"""Student to JSON with filter."""


class Student:
    """Student to JSON."""
    def __init__(self, first_name, last_name, age):
        """Initialize Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of Student."""
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """change attributes to student instance dict"""
        for key, value in json.item():
            setattr(self, key, value)
