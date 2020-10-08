from typing import Generator, Literal

def fibonacci() -> Generator[Literal[0, 1], None, None]:
    limit = int(4e6)
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

def even_fibonacci_sum() -> int:
    return sum(n for n in fibonacci() if n % 2 == 0)

print(even_fibonacci_sum())
