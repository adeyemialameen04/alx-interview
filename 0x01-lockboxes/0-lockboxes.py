#!/usr/bin/env python3
"""Documenting module"""


def canUnlockAll(boxes):
    """Documenting function"""
    n = len(boxes)  # Total number of boxes
    unlocked = {0}  # Box 0 is initially unlocked
    keys = boxes[0]  # Start with the keys in the first box

    # Explore keys until there are no more keys to process
    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:  # If the key is valid and unlocks a new box
            unlocked.add(key)  # Unlock the box
            keys.extend(boxes[key])  # Add the keys found in this box to explore further

    # Check if we have unlocked all boxes
    return len(unlocked) == n
