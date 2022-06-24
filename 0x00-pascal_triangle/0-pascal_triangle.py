#!/usr/bin/python3
"""return list of pascal triangle numbers"""


def pascal_triangle(n):
    """
        return a list of numbers representing pascal triangle
        param: n - size of triangle
    """

    iList = []
    if n <= 0:
        return iList  # Empty list

    for i in range(n):
        iList.append([])
        iList[i].append(1)

        for j in range(1, i):
            iList[i].append(iList[i-1][j-1]+iList[i-1][j])
        if(n != 0):
            iList[i].append(1)

    return iList
