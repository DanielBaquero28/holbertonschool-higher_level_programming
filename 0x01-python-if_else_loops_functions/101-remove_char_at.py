#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        copy_string = str[:n]
        copy_string += str[n+1:]
    else:
        copy_string = str
    return(copy_string)
