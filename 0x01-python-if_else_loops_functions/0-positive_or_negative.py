#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number >= 1:
    print("{} is positive".format(number))
elif number < 0:
    print("{} is negative".format(number))
else:
    print ("{} is zero".format(number))
