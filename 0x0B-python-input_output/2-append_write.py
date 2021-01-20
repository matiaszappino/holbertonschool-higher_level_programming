#!/usr/bin/python3
"""Append Write"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)"""
    with open(filename, 'a') as f:
        number_characters = f.write(text)
    return number_characters
