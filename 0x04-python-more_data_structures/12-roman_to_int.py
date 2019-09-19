#!/usr/bin/python3
def roman_to_int(roman_string):

    rom_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    val = 0
    for i in range(0, len(roman_string)):
        if i > 0 and rom_dic[roman_string[i]] > rom_dic[roman_string[i - 1]]:
            val += rom_dic[roman_string[i]] - 2 * rom_dic[roman_string[i - 1]]
        else:
            val += rom_dic[roman_string[i]]

    return (val)
