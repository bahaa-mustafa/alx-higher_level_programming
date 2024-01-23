#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
number = ("{}".format(number))
if int(number[-1]) > 5:
    print("Last digit of {} ".format(number), end="")
    print("is {} and is greater than 5".format(number[-1]))
elif int(number[-1]) == 0:
    print("Last digit of {} is {} and is 0".format(number, number[-1]))

elif int(number) < 0 and int(number[-1]) < 6:
    print("Last digit of {} ".format(number), end="")
    print("is -{} and is less than 6 and not 0".format(number[-1]))
else:
    print("Last digit of {} ".format(number), end="")
    print("is {} and is less than 6 and not 0".format(number[-1]))
