#!/usr/bin/python3
def remove_char_at(str, n):
    str_two = ""
    for i in range(len(str)):
        if i != n:
            str_two = str_two + str[i]
    return str_two
