#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = dict(a_dictionary)
    for i, j in new_dic.items():
        new_dic[i] = j*2
    return new_dic
