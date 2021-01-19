#!/usr/bin/python3
"""Inherits from"""


def inherits_from(obj, a_class):
    """True if the object is an instance of a class"""
    if obj.__class__ == a_class:
        return False
    else:
        return True
