#!/usr/bin/python3

# calculat length of string
# make loop on sring
# check if char. is upper ==> pass
# if not convert to upper by using ascii code: (ascii code - 32)

def uppercase(str):
    length = len(str)
    for c in range(0: length):
        if ord(str[c]) > 96 and ord(str[c]) < 123:
            str[c] = chr(ord(str[c]) - 32)
        else:
            pass
    print("{}".format(str))