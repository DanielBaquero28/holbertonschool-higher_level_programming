#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    my_list2 = set(my_list)

    return (reduce((lambda x, y: x+y), my_list2))
