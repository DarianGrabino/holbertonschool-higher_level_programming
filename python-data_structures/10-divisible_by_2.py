#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    while my_list:
        for n in range(0, len(my_list)):
            if my_list[n] % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
# append() colocará nuevos elementos en el espacio disponible
