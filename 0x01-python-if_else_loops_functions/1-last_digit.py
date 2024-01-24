#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

# if number >= 0 ===> if last digit > 5 print great than 5
# ===> if == 0 print is 0
# ===> if is less than 6 print less than 6
# elif number or last gidit == 0 print is 0
# else print -(last digit) less than 6


print("Last digit of {} ".format(number), end="")
number = ("{}".format(number))

if int(number[-1]) == 0:
    print("is {} and is 0".format(number[-1]))
elif int(number) < 0:
    print("is -{} and is less than 6 and not 0".format(number[-1]))
elif int(number[-1]) > 5:
    print("is {} and is greater than 5".format(number[-1]))
else:
    print("is {} and is less than 6 and not 0".format(number[-1]))
