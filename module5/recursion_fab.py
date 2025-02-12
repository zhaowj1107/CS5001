from typing import List
from timeit import default_timer as timer
import sys

def resurive_fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return resurive_fibonacci(n - 1) + resurive_fibonacci(n - 2)



def resurive_fibonacci_memo(n: int, memo: List[int] = None):
    if memo is None:
        memo = [-1] * (n + 1)
    
    if memo[n] != -1:
        return memo[n]

    if n == 0:
        memo[n] = 1
        return memo[n]
    elif n == 1:
        memo[n] = 1
        return memo[n]
    else:
        memo[n] = resurive_fibonacci_memo(n - 1, memo) + resurive_fibonacci_memo(n - 2, memo)
        return memo[n]
    

start = timer()
resurive_fibonacci(39)
end = timer()
print("The runtime of recursive fibonacci without memoization :", round(end - start,6), "seconds")


start = timer()
resurive_fibonacci_memo(39)
end = timer()
print("The runtime of recursive fibonacci with memoization :", round(end - start,6), "seconds")