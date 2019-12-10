#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
opp = number
if opp < 0:
        opp = -1 * opp
digit = opp % 10
if digit > 5:
        print("Last digit of {} is {} and greater then 5".format(number, digit))
elif digit == 0:
        print("Last digit of {} is {} and is 0".format(number, digit))
else:
        print("Last digit of {} is {} and is less then 6 and not 0".format(number, digit))
