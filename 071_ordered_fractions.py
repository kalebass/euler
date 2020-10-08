import numpy as np

def problem71() -> np.integer:
    ara = np.arange(1000001)
    ara[0] = 1
    values = 3 * ara // 7 / ara
    values[ara % 7 == 0] = 0
    return np.argmax(values)

print(problem71())
