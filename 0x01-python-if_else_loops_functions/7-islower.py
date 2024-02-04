#!/usr/bin/python3
# make a loop in ascii code for character [97:122]
# if it found pass else return false

def islower(c):
    if ord('{}'.format(c)) > 96 and ord('{}'.format(c)) < 123:
        return True

    elif not isinstance(c, chr):
        raise TypeError()
    else: #ord('{}'.format(c)) > 64 and ord('{}'.format(c)) < 91:
        return False
#    else:
#        raise TypeError()
