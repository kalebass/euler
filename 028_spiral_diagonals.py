def f(n: int) -> int:
    return int(4*n*(1 + 1/3*(n + 1)*(4*n + 7/2)) + 1)
print(f((1001 - 1) // 2))
