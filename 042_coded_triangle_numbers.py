import csv, numpy as np

def triangle_words(word_array: np.ndarray) -> np.ndarray:
    letters = word_array.view(dtype=np.uint8).reshape(-1, 14)
    letters[letters != 0] += 1 - ord('A')
    scores = letters.sum(axis=1)
    triangles = np.arange(20)*(np.arange(20) + 1) // 2
    return np.bincount(scores)[triangles].sum()

with open('p042_words.txt', newline='') as f:
    reader = csv.reader(f)
    arr = np.array(next(reader), dtype='|S14')

print(triangle_words(arr))
