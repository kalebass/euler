def res1():
    return sum(range(0, 1000, 3)) + sum(range(0, 1000, 5)) - sum(range(0, 1000, 15))

def res2():
    return 3*333*334//2 + 5*199*200//2 - 15*66*67//2

print(res1(), res2())
