#!/usr/bin/python3

# print two digit ===> digit one: start from 0
# ===>digit two: start from 1 && increament by one over inner loop
# gidit one increament by one ovet outer loop
# and inner loop increament one too

for n in range(0, 10):
    for i in range(1, 10):
        if n >= i:
            pass
        elif n == 8 and i == 9:
            print("{}{}".format(n, i))
        else:
            print("{}{}, ".format(n, i), end="")
