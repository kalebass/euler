def order(divisor: int, n: int = 10) -> int:
    i = 1
    remainder = n % divisor
    while remainder > 1:
        remainder = (n * remainder) % divisor
        i += 1
    return i

N = 1000
numbers = set(range(1, N, 2)) - set(range(5, N, 10))
print(max(numbers, key=order))
