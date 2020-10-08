import numpy as np

def p099(pairs):
    a = pairs[:, 1] * np.log(pairs[:, 0])
    return np.argmax(a) + 1

pairs = np.loadtxt('p099_base_exp.txt', dtype=int, delimiter=',')
print(p099(pairs))
