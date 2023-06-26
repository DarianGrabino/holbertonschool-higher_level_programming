#!/usr/bin/python3
""" obtener una representacion en forma de diccionario """


def class_to_json(obj):
    """ Esta función utiliza el atributo __dict__ de un objeto /
    para obtener una representación en forma de diccionario/
    de sus atributos y sus valores """
    return obj.__dict__
