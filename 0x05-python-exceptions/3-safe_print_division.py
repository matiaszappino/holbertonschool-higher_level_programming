#!/bin/usr/python3
def safe_print_division(a, b):
    try:
        c = a / b
        return c
    except:
        c = None
        return c
    finally:
        print("Inside result: {}".format(c))
