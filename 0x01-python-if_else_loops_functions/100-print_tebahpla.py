#!/usr/bin/python3
def yourStyle(i):
    if i % 2 == 0:
        return chr(i + 32)
    return chr(i)


for c in range(90, 64, -1):
    print("{}".format(yourStyle(c)), end="")
