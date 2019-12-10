#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
first_digit = number % 10
if first_digit > 5:
        print("Last digit of {} is greater then 5".format(number, first_digit))
elif first_digit == 0:
        print("Last digit of {} and is 0".format(number, first_digit))
else:
        print("Last digit of {} is less then 6 and not 0".format(number, first_digit))
