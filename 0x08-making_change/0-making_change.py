#!/usr/bin/python3
""" making change"""
# coins: list containg infinite numbe of coins
# total: the change to be given
# return: (int) min number of coins to meet totale else return -1
import sys


def makeChange(coins: list, total: int) -> int:
    """ find min coins to make change"""
    if total == 0:
        return 0
    size: int = len(coins)
    change: int = [0] * len(total + 1)
    change[0] = 0
    # initialize change values as infinite
    for i in range(1, total + 1):
        change[i] = sys.maxsize
    # find min coins required from 1 to total
    for i in range(1, total + 1):
        # go through all coins less than i
        for j in range(size):
            if coins[j] <= i:
                count: int = change[i - coins[j]]
                if count != sys.maxsize and count + 1 < change[i]:
                    change[i] = count + 1

    if change[total] == sys.maxsize:
        return -1
    return change[total]
