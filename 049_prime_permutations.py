from euler import primes_from_2_to

primes = primes_from_2_to(10000)[168:]
Np = len(primes)

for i in range(Np):
    for j in range(i + 1, Np):
        d = primes[j] - primes[i]
        n3 = primes[j] + d
        if n3 > 9999:
            break
        p1, p2 = primes[i], primes[j]
        if n3 in primes and set(str(p1)) == set(str(p2)) == set(str(n3)):
            print(p1, p2, n3)
