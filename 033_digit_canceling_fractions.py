import fractions

res = fractions.Fraction(1)

for den in range(10, 100):
    C, D = den // 10, den % 10
    if D != 0 and C != D:
        for num in range(10, den):
            A, B = num // 10, num % 10
            if B == C:
                # AB / CD
                f = fractions.Fraction(num, den)
                test = fractions.Fraction(A, D)
                if f == test:
                    res *= test
                    print(num, den)
print(res)
