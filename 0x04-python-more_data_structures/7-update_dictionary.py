#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dic = {}
    for i, j in a_dictionary.items():
        if i != key:
            new_dic[i] = a_dictionary[i]
        if i == key:
            new_dic[i] = value
        if key not in a_dictionary:
            new_dic[key] = value
    return new_dic
