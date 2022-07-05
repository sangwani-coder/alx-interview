#!/usr/bin/python3
""" Write a method to determine if boxes can be opened"""


def canUnlockAll(boxes):
    """ Chech if box is openable"""
    if len(boxes) == 0:
        return False

    box = [0]
    for keys in box:
        for key in boxes[keys]:
            if key not in box:
                if key < len(boxes):
                    box.append(key)
    if len(box) == len(boxes):
        return True

    return False
