#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list2 = set(my_list)
    result = 0
    for i in my_list2:
        result += i

    return (result)
