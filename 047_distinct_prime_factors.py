from math import sqrt, ceil

def factor(n: int) -> int:
    a = ceil(sqrt(n))
    b2 = a*a - n
    if a*a == n:
        return a
    b = int(sqrt(b2))
    while b*b != b2:
        a += 1
        b2 = a*a - n
        b = int(sqrt(b2))
    return a - b

def factors(n: int) -> set[int]:
    if n % 2 == 0:
        return { 2 }.union(factors(n // 2))
    f = factor(n)
    if f == 1:
        return {n}
    else:
        return factors(n // f).union(factors(f))

consecutive = 0
for n in range(130000, 250000):
    if len(factors(n)) == 4:
        consecutive += 1
    else:
        consecutive = 0
    if consecutive == 4:
        print(n)
        break
