def d(n: int) -> int:
    return sum(d for d in range(1, n//2 + 1) if n % d == 0)

N = 10000
dlist = [d(n) for n in range(N)]
dlist[0] = 0

amicable_sum = 0
for i in range(N):
    divsum = dlist[i]
    if divsum < N and dlist[divsum] == i and divsum != i:
        amicable_sum += i
        print((i, divsum))
print(amicable_sum)
