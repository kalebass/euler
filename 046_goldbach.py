import numpy as np
from euler import primes_from_2_to

N = 20000
ara = np.arange(N)
primes = primesfrom2to(N)
oddcmp = np.setdiff1d(np.arange(9, N, 2), primes, assume_unique=True)
squares = np.arange(int((N // 2) ** 0.5)) ** 2
diffs = oddcmp[:, np.newaxis] - 2*squares

for row in diffs:
    diff2 = row[:, np.newaxis] - primes
    if 0 not in diff2:
        print(row[0])
        break
