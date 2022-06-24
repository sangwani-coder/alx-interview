#!/usr/bin/python3
"""print pascal triangle"""

def pascal_triangle(n):
    """
        print pascal triangle
        param: n - size of triangle
    """
    for i in range(n + 1):
        for j in range(n - 1):
            print(" ", end="")
        C = 1
        for j in range(1, i + 1):
            print(C, ' ', sep='', end="")
            C = C * (i - j) // j
        print()
