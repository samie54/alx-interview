#!/usr/bin/python3


"""
Mini number of ops
"""


def minOperations(n: int) -> int:
    """
    minimum opeartions to run determined.
    Args:
        n (int):
    Returns:
        Returns an int
    """
    if not isinstance(n, int):
        raise TypeError('Expected an integer')
    if n < 2:
        return 0
    operations, root = 0, 2
    while root <= n:
        if n % root == 0:
            operations += root
            n = n / root
            root -= 1
        root += 1
    return operations
