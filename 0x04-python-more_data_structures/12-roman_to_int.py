#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    num = 0

    if type(roman_string) is not str or roman_string is None:
        return 0
    if len(roman_string) == 1:
        return rom_dic.get(roman_string)
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i + 2] in rom_dic:
            num += rom_dic[roman_string[i:i + 2]]
            i += 2
        else:
            num += rom_dic[roman_string[i]]
            i += 1
    return num
