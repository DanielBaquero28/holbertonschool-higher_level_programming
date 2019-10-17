#!/usr/bin/python3
import math


def combination(n, r):
    return (int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r))))

def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return (" ")
    for count in range(n):
        row = []
        for item in range(count + 1):
            row.append(combination(count, item))
        triangle.append(row)

    return (triangle)
