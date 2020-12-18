#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    for i in range(len(roman_string)):
        if i > 0 and rom_dic[roman_string[i]] > rom_dic[roman_string[i - 1]:
            integer += (rom_dic[roman_string[i]] - 2 * rom_dic[roman_string[i - 1]])
        else:
            integer += rom_dic[roman_string[i]]
    return integer
