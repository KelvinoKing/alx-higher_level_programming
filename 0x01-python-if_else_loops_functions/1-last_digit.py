#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = 0

if number < 0:
    last = -(abs(number) % 10)
elif number >= 0:
    last = abs(number) % 10

if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))
elif last == 0:
    print("Last digit of {} is {} and is 0".format(number, last))
elif last < 6 and last != 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
