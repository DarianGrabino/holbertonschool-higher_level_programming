#!/usr/bin/python3
"""class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines an initialization method"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """method so that it returns [Square]"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    def area(self):
        """function that return area"""
        return self.size ** 2

    def display(self):
        """function that print a square with character #"""
        for j in range(self.y):
            print()
        for n in range(self.size):
            for m in range(self.x):
                print(" ", end="")
            for i in range(self.size):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """update argument order"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary with keys and values"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
