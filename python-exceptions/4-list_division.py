#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for n in range(list_length):
        try:
            result.append(my_list_1[n] / my_list_2[n])
        except (ZeroDivisionError):
            print("division by 0")
            result.append(0)
        except (ValueError, TypeError):
            print("out of range")
            result.append(0)
        except (IndexError):
            print("wrong type")
            result.append(0)
        finally:
            pass
    return result
