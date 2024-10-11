#!/usr/bin/python3
"""Documenting module"""


def canUnlockAll(boxes):
    """Documenting function"""
    n = len(boxes)
    unlocked = {0}
    keys = boxes[0]

    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])

            # Check if we have unlocked all boxes
    return len(unlocked) == n
