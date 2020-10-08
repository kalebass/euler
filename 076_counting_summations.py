from typing import Union
import numpy as np

memo = np.zeros((101, 101), dtype=np.int32)

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

print(partitions(100))
