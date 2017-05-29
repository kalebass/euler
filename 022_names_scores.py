import csv
import numpy as np

with open('p022_names.txt') as f:
    reader = csv.reader(f, delimiter=',')
    names = np.array(next(reader), dtype='|S11')

def score(names):
    names.sort()
    names = names.view(dtype=np.uint8).reshape(-1, 11)
    names[names != 0] -= 64
    score = np.sum(names, axis=1) * np.arange(1, names.shape[0] + 1)
    return np.sum(score)

print(score(names))
