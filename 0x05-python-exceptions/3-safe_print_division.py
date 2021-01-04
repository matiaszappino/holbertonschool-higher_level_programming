#!/bin/usr/python3
def safe_print_division(a, b):
    c = None
    try:
        c = a / b
        return c
    except:
        return None
    finally:
        print("Inside result: {}".format(c))
