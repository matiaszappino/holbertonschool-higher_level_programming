#!/usr/bin/python3
"""Append After"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file"""
    inputfile = open(filename, 'r').readlines()
    write_file = open(filename, 'w')
    for line in inputfile:
        write_file.write(line)
        if search_string in line:
            write_file.write(new_string)
    write_file.close()
