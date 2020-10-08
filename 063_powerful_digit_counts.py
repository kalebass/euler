from math import log10

result = sum(int(1/(1 - log10(npowers))) for npowers in range(1, 10))
print(result)
