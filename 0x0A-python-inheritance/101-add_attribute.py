#!/usr/bin/python3
"""Adds a new attribute to an object if it’s possible"""


def add_attribute(object, name, value):
    """Adds a new attribute"""
    try:
        object.name = value
    except:
        raise TypeError("can't add new attribute")
