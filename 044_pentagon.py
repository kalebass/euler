import numpy as np

N = 5000
ara = np.arange(N)
pentagons = ara * (3 * ara - 1) // 2
mindiff = np.inf
for k in range(2, N):
    j = k - 1
    Pj, Pk = pentagons[j], pentagons[k]
    if Pk - Pj > mindiff:
        break
    while Pk - Pj < mindiff and j >= 1:
        if Pk - Pj in pentagons and Pj + Pk in pentagons:
            print(Pj, Pk)
            mindiff = Pk - Pj
            break
        j -= 1
        Pj = pentagons[j]
print(mindiff)
