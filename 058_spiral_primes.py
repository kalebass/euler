import itertools
from math import sqrt
from euler import is_prime

def spiral_diagonals():
    res = 1
    yield res
    for i in itertools.count(start=2, step=2):
        for j in range(4):
            res += i
            yield res

def result():
    primes = 0
    total = 1
    dg = spiral_diagonals()
    next(dg)
    for i in itertools.count(start=1, step=2):
        for j in range(4):
            d = next(dg)
#            print(d)
            if is_prime(d):
                primes += 1
        total += 4
        ratio = primes / total
#        print(ratio)
        if ratio < 0.1:
            return int(sqrt(d))

print(result())
