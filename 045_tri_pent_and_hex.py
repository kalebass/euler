import numpy as np

def p045() -> np.integer:
    ara = np.arange(40000, dtype=np.int64)
    pent = ara*(3*ara - 1) // 2
    hexa = ara*(2*ara - 1)
    tph = np.intersect1d(pent, hexa, assume_unique=True)
    return tph.max()

print(p045())
