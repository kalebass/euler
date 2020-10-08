from math import factorial

s = sum(n for n in range(3, 2600000) if n == sum(factorial(int(d)) for d in str(n)))
print(s)
