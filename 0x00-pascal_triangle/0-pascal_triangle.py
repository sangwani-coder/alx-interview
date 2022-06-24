#!/usr/bin/python3
"""return list of pascal triangle numbers"""


def pascal_triangle(n):
    """
        return a list of numbers representing pascal triangle
        param: n - size of triangle
    """

    listOfIntegers = []
    if n <= 0:
        return listOfIntegers # Empty list

    for i in range(n):
        listOfIntegers.append([])
        listOfIntegers[i].append(1)

        for j in range(1,i):
            listOfIntegers[i].append(listOfIntegers[i-1][j-1]+listOfIntegers[i-1][j])
        if(n!=0):
            listOfIntegers[i].append(1)

    return listOfIntegers
