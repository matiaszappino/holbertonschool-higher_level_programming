#!/usr/bin/python3
"""Test Module"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()


def add_integer(a, b=98):
    """Function add integer"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
