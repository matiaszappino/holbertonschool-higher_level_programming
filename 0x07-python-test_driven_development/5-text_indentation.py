#!/usr/bin/python3
"""Test Module"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()

def text_indentation(text):
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print('\n')
        else:
            print(i, end="")