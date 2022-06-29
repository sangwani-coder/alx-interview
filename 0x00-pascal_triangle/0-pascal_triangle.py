#!/usr/bin/python3
"""return list of pascal triangle numbers"""


def pascal_triangle(n: int) -> list:
    """
        return a list of numbers representing pascal triangle
        param: n - size of triangle
    """

    iList = []
    if n <= 0:
        return iList  # Empty list

    for i in range(n):
        iList.append([])
        iList[i].append(1)  # append 1 as first number in each list

        for j in range(1, i):
            iList[i].append(iList[i-1][j-1]+iList[i-1][j])
        if(n != 0):
            if i == 0:  # skip adding another 1 to first list in iList
                continue
            iList[i].append(1)  # Append 1 as last number in each list
    return iList
