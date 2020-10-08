import itertools
from typing import Generator
from euler import is_prime

digits = '1234567'

def pandigital_primes() -> Generator[int, None, None]:
    for n in itertools.permutations(digits):
        n = int(''.join(n))
        if is_prime(n):
            yield n

print(max(n for n in pandigital_primes()))
