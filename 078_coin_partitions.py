from typing import Union
import numpy as np

memo = np.zeros((1001, 1001), dtype=np.int64)

def partitions(n: int) -> Union[np.integer, int]:
    def ppart(n: int, m: int) -> Union[np.integer, int]:
        if n <= 1:
            return 1
        if m > n:
            m = n
        if memo[n, m] == 0:
            memo[n, m] = sum(ppart(n - k, k) for k in range(1, m + 1))
        return memo[n, m]
    return ppart(n, n)

def p078():
    for i in range(0, 400):
        if partitions(i) % 1000000 == 0:
            return i

print(p078())
