#!/usr/bin/python3
"""
Function's name: lazy_matrix_mul

Test command: python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Return:
    Multiplication of both matrices
    """
    return (np.dot(m_a, m_b))
