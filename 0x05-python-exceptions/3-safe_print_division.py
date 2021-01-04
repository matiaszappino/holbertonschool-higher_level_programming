#!/bin/usr/python3
def safe_print_division(a, b):
    try:
        c = a / b
        return c
    except (ZeroDivisionError, ValueError):
        c = None
    finally:
        print("Inside result: {}".format(c))
    return c
