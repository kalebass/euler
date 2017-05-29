import numpy as np
from numpy.lib.stride_tricks import as_strided

def p008():
    n = np.fromfile('p008.bin', dtype=np.uint8)
    return as_strided(n, (13, 1000 - 12), (1, 1)).prod(0, np.int64).max()

print(p008())
