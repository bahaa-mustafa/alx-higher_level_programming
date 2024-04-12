#!/usr/bin/python3
def convert_lower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return chr(ord(c) - 32)
    else:
        return c

def uppercase(str):
    for c in str:
        print("{}".format(convert_lower(c)), end="")
    print("")
