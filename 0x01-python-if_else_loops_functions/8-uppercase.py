#!/usr/bin/python3

def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False

# calculat length of string
# make loop on sring
# check if char. is upper ==> pass
# if not convert to upper by using ascii code: (ascii code - 32)

def uppercase(str):
    for c in str:
        print("{:c}"
                .format(ord(c)) if not islower(c) else (ord(c) - 32),end="")
    print("")
