#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)
    if len_list == 0:
        return (None)

    my_list.sort()
    max_number = my_list[-1]
    return (max_number)
