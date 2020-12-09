#!/usr/bin/python3
def remove_char_at(str, n):
    str_two = ""
    for i in str:
        if i != n:
            char = chr(ord(i))
            str_two = str_two + char
    return str_two
