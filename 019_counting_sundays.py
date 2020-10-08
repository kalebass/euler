import numpy as np

def sundays() -> np.integer:
    year = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    century = np.tile(year, (100, 1))
    century[3::4, 1] = 29
    cumdays = np.cumsum(century)
    cumdays += 365 - cumdays[0]
    weekdays = cumdays % 7
    return np.sum(weekdays == 6)

print(sundays())
