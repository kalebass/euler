import numpy as np

def largest_product():
    arr = np.loadtxt('p011.txt', dtype=np.int32)
    
    return max(
        np.amax(arr[:-3] * arr[1:-2] * arr[2:-1] * arr[3:]),
        np.amax(arr[:, :-3] * arr[:, 1:-2] * arr[:, 2:-1] * arr[:, 3:]),
        np.amax(arr[:-3, :-3] * arr[1:-2, 1:-2] * arr[2:-1, 2:-1] * arr[3:, 3:]),
        np.amax(arr[:-3, 3:] * arr[1:-2, 2:-1] * arr[2:-1, 1:-2] * arr[3:, :-3]),
    )

print(largest_product())
