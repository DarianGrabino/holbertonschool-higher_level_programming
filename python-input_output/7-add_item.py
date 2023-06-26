#!/usr/bin/python3
"""Load, add, save."""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Cargamos los elementos existentes desde el archivo, o creamos una lista vacía
try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

# Agregamos los nuevos elementos a la lista
for arg in sys.argv[1:]:
    items.append(arg)

# Guardamos la lista actualizada en el archivo
save_to_json_file(items, "add_item.json")
