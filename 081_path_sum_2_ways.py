import numpy as np

def min_path_sum(arr):
    def min_sum_rec(arr):
        N = arr.shape[0]
        if N == 1:
            return arr[0, 0]
        edge = N - 2
        arr[edge, edge] += min(arr[edge + 1, edge], arr[edge, edge + 1])
        for i in reversed(range(N - 2)):
            arr[i, edge] += min(arr[i + 1, edge], arr[i, edge + 1])
            arr[edge, i] += min(arr[edge + 1, i], arr[edge, i + 1])
        return min_sum_rec(arr[:-1, :-1])

    arr[-1, ::-1] = np.cumsum(arr[-1, ::-1])
    arr[::-1, -1] = np.cumsum(arr[::-1, -1])
    return min_sum_rec(arr)

A = np.loadtxt('p081_matrix.txt', dtype=int, delimiter=',')
print(min_path_sum(A))
