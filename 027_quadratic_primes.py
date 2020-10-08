import numpy as np
from numpy import ma

nprimes = 100000
primes = ma.array(np.arange(nprimes, dtype=np.int32))
for i in primes[2 : nprimes//2]:
    if not i:
        continue
    # print(i)
    mask = np.zeros_like(primes, dtype=np.bool, subok=False)
    mask[i+1:][primes[i+1:] % i == 0] = True
    # print(mask)
    primes[mask] = ma.masked
    # print(primes)

def consecutive(a: int, b: int) -> int:
    consecutive = 0
    for n in range(1000):
        value = (n + a) * n + b
        if not value in primes[:5000]:
            break
        consecutive += 1
    return consecutive

#print(consecutive(-79, 1601))

N = 1000
maxConsecutive = 0
for a in range(-N, N):
    print(a, end=' ')
    for b in range(-N, N):
        result = consecutive(a, b)
        if result > maxConsecutive:
            print('\nn^2 +', a, '* n +', b, 'gives', result, 'primes')
            maxConsecutive = result
            maxa, maxb = a, b
