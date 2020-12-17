#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for i in set_1:
        if i not in set_2:
            new_set.append(i)
    for j in set_2:
        if j not in set_1 and j not in new_set:
            new_set.append(j)
    return new_set
