#!/usr/bin/python3
""" making change
    coins: list containg infinite numbe of coins
    total: the change to be given
    return: fewest number of coins needed to meet total, otherwise return -1
"""
#import sys


def makeChange(coins: list, total: int) -> int:
    """ find min coins to make change"""
    if total == 0:
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

