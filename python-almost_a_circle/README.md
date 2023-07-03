## Task 1
class Base:
    __nb_objects = 0
### Defines a private class attribute with an initialvalue of 0. This will beused to count the total number of objects of class
    def __init__(self, id=None):
### Defines an initialization method, it will be executed each time a new object of the Base class is created.The argument self is a reference to the current object and id will be used to set the unique identifier of the object
        if id is None:
            self.id = id
            self.__nb_objects += 1

