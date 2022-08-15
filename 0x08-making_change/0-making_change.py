#!/usr/bin/python3
""" 
find the minimum number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """Make change module"""
    if total <= 0:
        return 0
    MAX = total + 1
    size: int = len(coins)
    change: int = [0] * (total + 1)
    change[0] = 0
    # initialize change values as infinite
    for i in range(1, total + 1):
        change[i] = MAX
    # find min coins required from 1 to total
    for i in range(1, total + 1):
        # go through all coins less than i
        for j in range(size):
            if coins[j] <= i:
                count: int = change[i - coins[j]]
                if count != MAX and count + 1 < change[i]:
                    change[i] = count + 1

    if change[total] == MAX:
        return -1
    return change[total]
