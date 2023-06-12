#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for n in range(0, len(new_list)):
        if new_list[n] == search:
            new_list[n] = replace
    return new_list
