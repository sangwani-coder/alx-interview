#!/usr/bin/python3
""" make change"""

def makeChange(coins: list, total: int) -> int:
    """ find min coins to make change"""
    count = 0
    coin = 0
    stack = []
    if total <= 0:
        return count
    for i in range(len(coins)):
        if coins[0] == total:
            count += 1
            return count
        if coins[i] > total:
            continue
        else:
            x = subtract(total, coins[i], count)
            total = x[0]
            count = x[1]

    if total == 0 and count > 0:
        return count
    return -1

def subtract(total: int, value: int, count: int):
    while total >= value:
        total -= value
        count += 1

    return list([total, count])

