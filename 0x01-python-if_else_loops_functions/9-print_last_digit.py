#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        module = number % 10
    elif number < 0:
        module = (number * -1) % 10
    print("{:d}".format(module), end="")
    return module
