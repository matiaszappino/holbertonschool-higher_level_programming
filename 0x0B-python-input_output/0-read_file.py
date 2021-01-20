#!/usr/bin/python3
"""Read File"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r') as f:
        print(f.read())
