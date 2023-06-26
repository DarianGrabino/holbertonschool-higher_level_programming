#!/usr/bin/python3
""" Método de inicialización que se llama al/
 crear una instancia de la clase Estudiante """


class Student:
    def __init__(self, first_name, last_name, age):
        """ Toma tres argumentos, establece las propiedades de/
            la instancia con valores de los argumentos """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ devuelve un diccionario que representa los/
         atributos de un objeto """
        return self.__dict__
