#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    num = 0

    if type(roman_string) is not str or roman_string is None:
        return 0
    if len(roman_string) == 1:
        return rom_dic.get(roman_string)
    for i in range(len(roman_string)):
        if i + 1 == len(roman_string):
            num += rom_dic.get(roman_string[i])
        elif rom_dic.get(roman_string[i]) >= rom_dic.get(roman_string[i + 1]):
            num += rom_dic.get(roman_string[i])
        else:
            num -= rom_dic.get(roman_string[i])    
    return num
