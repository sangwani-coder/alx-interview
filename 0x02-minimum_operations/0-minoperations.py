#!/usr/bin/python3
"""
    Implemnets a Depth First Search Algorithm that
    calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
        calculates the fewest number of operations needed to result
        in exactly n H characters in the file. and returns
        an integer, if n is impossible to reach, return 0
    """

    def dfs(n: int):
        if n == 1 or n > 10000:
            return 0
        for i in range(n // 2, 0, -1):
            if n % i == 0:
                return 1 + ((n // i) - 1) + dfs(i)  # copy, paste
                # Here 1 is for copy the all previous, for example,
                # n is 21, i is 7.
                # We used 1 step to copy all 7's
                # ((n // i) - 1) is (21 // 7) - 1. Here we have 7 already,
                # used 2 steps to paste 7's
                # To get 7's on the notepad, we need dfs(7) steps.
    return dfs(n)
