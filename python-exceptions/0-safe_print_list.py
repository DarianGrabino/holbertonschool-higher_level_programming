#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        element = 0
        for element in my_list:
            print(element, end="")
            element += 1
            if count == x:
                break
    except IndexError:
        pass
    print()
    return element
