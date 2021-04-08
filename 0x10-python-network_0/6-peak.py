#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    array_len = len(list_of_integers)
    if (array_len == 1):
        return array_len[0]
    elif (array_len == 2):
        if (list_of_integers[1] >= list_of_integers[0]):
            return list_of_integers[1]
    else:
        elem = 1
        for elem in range(len(list_of_integers) - 1):
            if list_of_integers[elem] >= list_of_integers[elem + 1] and list_of_integers[elem] >= list_of_integers[elem - 1]:
                return list_of_integers[elem]
