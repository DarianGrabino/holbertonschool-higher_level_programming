#!/usr/bin/python3

def uppercase(str):
    result = ""
    for n in str:
        if ord(n) >= 92 and ord(n) <= 122:
            result += chr(ord(n) - 32)
        else:
            result += n
    print("{}".format(result))
