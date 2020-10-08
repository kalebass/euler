import numpy as np
from math import ceil, sqrt

def primes_from_2_to(n: int) -> np.ndarray:
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[      ((k * k) // 3)      ::2*k] = False
            sieve[(k*k + 4*k - 2*k*(i&1))//3::2*k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)]

def primes_to(n: int) -> list[int]:
    sieve = n * [True]
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i : : 2*i] = ((n - i*i - 1) // (2*i) + 1) * [False]
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def is_prime(n: int) -> bool:
    for div in range(2, int(n**0.5) + 1):
        if n % div == 0:
            return False
    if n == 1:
        return False
    return True

def factor(n: int) -> int:
    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2
        return n
    a = ceil(sqrt(n))
    b2 = a*a - n
    b = int(sqrt(b2))
    while b*b != b2:
        a += 1
        b2 = a*a - n
        b = int(sqrt(b2))
    return a - b
