#!/usr/bin/python3

# calculat length of string
# make loop on sring
# check if char. is upper ==> pass
# if not convert to upper by using ascii code: (ascii code - 32)

def uppercase(str):
    for c in range(0: len(str)):
        if ord('{}'.format(str[c])) > 96 and ord('{}'.format(str[c])) < 123:
            str[c] = chr(ord('{}'.format(str[c])) - 32)
            print("{}".format(str[c]))
        else:
            print("{}".format(str[c]))
