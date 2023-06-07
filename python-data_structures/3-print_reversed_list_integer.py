#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reverse_list = my_list[::-1]
    for n in reverse_list:
        print("{}".format(n))
