#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)
    return sum(unique_numbers)
# set() se usa para convertir cualquiera de los elementos iterables
# en una secuencia de elementos iterables con elementos distintos
# sum() suma los numeros de la lista
