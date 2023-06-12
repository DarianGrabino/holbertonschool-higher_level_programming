#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keys in sorted(a_dictionary):
        print("{}: {}".format(keys, a_dictionary.get(keys)))
# sorted() devuelve una lista ordenada del objeto iterable especificados
# get() devuelve el valor de la clave dada si está presente en el diccionario
