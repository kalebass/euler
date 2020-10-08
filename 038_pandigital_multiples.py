import numpy as np

def scalar_range(nproducts: int):
    mod = 9 % nproducts
    if mod == 0:
        min_scalar = 10**(9 // nproducts - 1)
        max_scalar = 10**(9 // nproducts) // nproducts
    else:
        min_scalar = 10**(9 // nproducts) // (nproducts - mod + 1)
        max_scalar = 10**(9 // (nproducts)) // (nproducts - mod)
    return np.arange(min_scalar, max_scalar + 1)

def pandigital_multiples():
    pandigitals = []
    for nproducts in range(2, 10):
        products = np.outer(scalar_range(nproducts), np.arange(1, nproducts + 1))
        for p in products:
            pstr = ''.join(p.astype(str))
            if set(pstr) == set('123456789'):
                pandigitals.append(pstr)
    return max(pandigitals)

print(pandigital_multiples())
