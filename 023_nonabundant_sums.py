import numpy as np

def d(n: int):
    return sum(d for d in range(1, n//2 + 1) if n % d == 0)

limit = 28123
abundant = np.array([n for n in range(limit) if d(n) > n], dtype=np.uint32)
summable = abundant + abundant[:, np.newaxis]
summable = set(summable.ravel())
unsummable = set(range(limit)) - summable
print(sum(list(unsummable)))
