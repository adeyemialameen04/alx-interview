#!/usr/bin/python3
"""Documenting module"""


def minOperations(n):
    """min operations"""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Reduce n by dividing it by its smallest factors
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
