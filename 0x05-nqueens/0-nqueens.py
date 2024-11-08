#!/usr/bin/python3
import sys


def print_solution(board):
    """Prints the solution in the required format"""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row] == col:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]"""
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row):
    """Recursively solves the N Queens problem"""
    if row == len(board):
        print_solution(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)
            board[row] = -1  # Backtrack
