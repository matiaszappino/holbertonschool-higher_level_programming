#!/usr/bin/python3
"""Write File"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters"""
    with open(filename, 'w') as f:
        number_characters = f.write(text)
    return number_characters