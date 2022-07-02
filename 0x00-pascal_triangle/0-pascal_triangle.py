#!/usr/bin/python3
"""return list of pascal triangle numbers"""


def pascal_triangle(n: int) -> list:
    """
        return a list of numbers representing pascal triangle
        param: n - size of triangle
    """

    iList = []
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            if j == 0 or j == i - 1:
                row.append(1)
            else:
                n = iList[i - 2][j - 1] + iList[i -2][j]
                row.append(n)
        iList.append(row)

    return iList
