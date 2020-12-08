#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
if lastdigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastdigit))
if lastdigit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastdigit))
if lastdigit < 6 and lastdigit != 0 or lastdigit < 0:
    if lastdigit < 0:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0"
              .format(number, lastdigit * -1))
    else:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0"
              .format(number, lastdigit))
