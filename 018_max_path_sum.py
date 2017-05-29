import numpy as np

triangle = np.loadtxt('p067_triangle.txt', dtype=int)
nrows = len(triangle)
for i in range(nrows - 2, -1, -1):
    for j in range(i + 1):
        triangle[i, j] += np.amax(triangle[i+1, j:j+2])

print(triangle[0, 0])
