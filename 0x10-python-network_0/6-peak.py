#!/usr/bin/env python3
def help_find_peak(array_int, low, high, size):
    """ Function that calculates peak elements """
    middle = (low + high)/2
    middle = int(middle)
    if ((middle == 0 or array_int[middle - 1] <= array_int[middle])
        and (middle == size - 1 or array_int[middle + 1] <= array_int[middle])):
        return middle
    elif (middle > 0 and array_int[middle - 1] > array_int[middle]):
        return (help_find_peak(array_int, low, (middle - 1), size))
    else:
        return (help_find_peak(array_int, (middle + 1), high, size))

def find_peak(list_of_integers):
    """ Recursive function calling help function """
    n = len(list_of_integers)

    return help_find_peak(list_of_integers, 0, n - 1, n)
