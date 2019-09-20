#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_mul = 0
    sum_sec = 0
    for number in my_list:
        sum_mul += number[0] * number[1]
        sum_sec += number[1]

    return (sum_mul / sum_sec)
