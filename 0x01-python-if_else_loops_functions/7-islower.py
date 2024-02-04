#!/usr/bin/python3
# make a loop in ascii code for character [97:122]
# if it found pass else return false

def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
