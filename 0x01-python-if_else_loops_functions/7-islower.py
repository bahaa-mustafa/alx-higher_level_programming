#!/usr/bin/python3
# make a loop in ascii code for character [97:122]
# if it found pass else return false

def islower(c):
    for char in range(97: 123):
        if chr(char) == c:
            return True
        else:
            return False
