#!/usr/bin/pyton3

def new_in_list(my_list, idx, element):
    new_list = []
    for c in my_list:
        new_list.append(c)

    if idx < 0 or idx > len(my_list):
        return None
    else:
        new_list[idx] = element
        return new_list
