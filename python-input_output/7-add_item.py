#!/usr/bin/python3
"""Load, add, save."""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Cargamos los elementos existentes desde el archivo, o creamos una lista vacía
filename = "add_item.json"
try:
    lista = load_from_json_file(filename)
except FileNotFoundError:
    lista = []

# Agregamos los nuevos elementos a la lista
for arg in sys.argv[1:]:
    lista.append(arg)

# Guardamos la lista actualizada en el archivo
save_to_json_file(lista, filename)
