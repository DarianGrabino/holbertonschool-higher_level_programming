#!/usr/bin/python3
"""class Rectangule that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """defines an initialization method"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter"""
        return self.__width

    @property
    def height(self):
        """getter"""
        return self.__height

    @property
    def x(self):
        """getter"""
        return self.__x

    @property
    def y(self):
        """getter"""
        return self.__y

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """function that calculates the area"""
        return self.__width * self.__height

    def display(self):
        """function that print rectangle with the character #"""
        for j in range(self.__y):
            print()
        for n in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """method so that it returns [Rectangle]"""
        width = self.width
        height = self.height
        x = self.x
        y = self.y
        return (f"[Rectangle] ({self.id}) {x}/{y} - {width}/{height}")

    def update(self, *args, **kwargs):
        """update argument order"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
        # establece el valor de un atributo de un objeto en tiempo de ejecución

    def to_dictionary(self):
        """dictionary with keys and values"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
