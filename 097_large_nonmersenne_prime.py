def result() -> int:
    n = 1
    for i in range(7830450 // 10):
        n <<= 10
        n %= 10_000_000_000
    n <<= 7
    n *= 28433
    n += 1
    n %= 10_000_000_000
    return n

print(result())
