#!/usr/bin/python3
def max_integer(my_list=[]):
    while my_list:
        max = my_list[0]
        for n in range(0, len(my_list)):
            if max < my_list[n]:
                max = my_list[n]
        return max
