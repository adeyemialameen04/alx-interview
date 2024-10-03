#!/usr/bin/python3
"""
0-main
"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]
    
    for i in range(1, n):
        # Start each row with 1
        row = [1]
        # Fill in the middle elements
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with 1
        row.append(1)
        triangle.append(row)
    
    return triangle
