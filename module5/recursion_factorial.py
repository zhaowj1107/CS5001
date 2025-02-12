from typing import List

def factorial_memoization_list(n: int, memo: List[int] = None) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    if memo is None:
        memo = [-1] * (n + 1)

    if memo[n] != -1:
        return memo[n]

    if n == 0:
        memo[n] = 1
    else:
        memo[n] = n * factorial_memoization_list(n - 1, memo)

    return memo[n]

def factorial_memoization_list(n: int, memo: list = None) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    if memo is None:
        memo = [-1] * (n + 1)

    if memo[n] != -1:
        return memo[n]

    if n == 0:
        memo[n] = 1
    else:
        memo[n] = n * factorial_memoization_list(n - 1, memo)

    return memo[n]