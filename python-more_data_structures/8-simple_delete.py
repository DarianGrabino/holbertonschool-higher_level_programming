#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
    return a_dictionary
# pop() elimina y retorna un elemento de una lista,
# especificar índice a ser eliminado de la lista,
# si no se especifica ningún índice
# elimina y retorna el último elemento de la lista
