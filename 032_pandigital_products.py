from itertools import permutations

digits = set('123456789')
count = 0
for product_length in range(1, len(digits)):
    for prod in permutations(digits, product_length):
        p = int(''.join(prod))
        factor_digits = digits - set(prod)
        for factor1_length in range(1, len(factor_digits)):
            for factor1 in permutations(factor_digits, factor1_length):
                f1 = int(''.join(factor1))
                factor2_digits = factor_digits - set(factor1)
                for factor2 in permutations(factor2_digits):
                    f2 = int(''.join(factor2))
                    if f1 * f2 == p:
                        print(f1, '·', f2, '=', p)
