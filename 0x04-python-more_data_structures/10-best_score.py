#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new_dic = sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)
        return new_dic[0][0]
    else:
        return None
