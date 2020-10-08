from sympy.ntheory import totient

print(max(range(1, 1000000), key=lambda n: n / totient(n)))
