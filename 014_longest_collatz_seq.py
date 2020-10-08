def steps(n: int) -> int:
    s = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        s += 1
    return s

print(max(range(1, 10**6), key=steps))
