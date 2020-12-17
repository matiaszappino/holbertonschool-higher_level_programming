#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = []
    for i in set_1:
        if i in set_2:
            new_set.append(i)
    for j in set_2:
        if j in set_1 and j not in new_set:
            new_set.append(j)
    return new_set
