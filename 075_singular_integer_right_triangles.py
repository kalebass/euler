import numpy as np

def perimeter_counts(plimit: int) -> np.integer:
    uad = np.array(
    [[[ 1,  2,  2],
      [-2, -1, -2],
      [ 2,  2,  3]],
     [[ 1,  2,  2],
      [ 2,  1,  2],
      [ 2,  2,  3]],
     [[-1, -2, -2],
      [ 2,  1,  2],
      [ 2,  2,  3]]]
    )
    lengths = np.zeros(plimit, dtype=int)

    def count_branch(triple):
        perimeter = triple[0] + triple[1] + triple[2]
        if perimeter < plimit:
            lengths[::perimeter] += 1
            newtris = np.dot(triple, uad)
            count_branch(newtris[0])
            count_branch(newtris[1])
            count_branch(newtris[2])
    count_branch(np.array([3, 4, 5]))
    return (lengths == 1).sum()

print(perimeter_counts(1500001))
