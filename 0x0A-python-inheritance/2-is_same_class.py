#!/usr/bin/python3
"""Is the same class"""


def is_same_class(obj, a_class):
    """True if the object is exactly an instance of the specified"""
    if obj.__class__ == a_class:
        return True
    else:
        return False
