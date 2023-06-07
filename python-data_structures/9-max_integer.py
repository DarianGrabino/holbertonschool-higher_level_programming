#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max = 0
        for n in my_list:
            if n > max:
                max = n
        return max
