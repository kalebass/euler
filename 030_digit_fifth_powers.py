def digit_sum(n: int, exp: int) -> int:
    return sum(int(d)**exp for d in str(n))

s = sum(n for n in range(2, 400000) if digit_sum(n, 5) == n)
print(s)
