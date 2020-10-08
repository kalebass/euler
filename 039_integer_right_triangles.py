import numpy as np

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

def solutions(ptarget: int, triple: np.ndarray = np.array([3, 4, 5])) -> int:
    p = triple[0] + triple[1] + triple[2]
    if p < ptarget:
        multiple = 1 if ptarget % p == 0 else 0
        newtris = triple @ uad
        return (
            multiple
            + solutions(ptarget, newtris[0])
            + solutions(ptarget, newtris[1])
            + solutions(ptarget, newtris[2])
        )
    elif p > ptarget:
        return 0
    return 1

print(max(range(1001), key=solutions))
