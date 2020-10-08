from euler import primes_from_2_to, is_prime

def truncatable(prime: int):
    pstr = str(prime)
    for n in range(1, len(pstr)):
        truncatedR = int(pstr[n:])
        truncatedL = int(pstr[:-n])
        if not is_prime(truncatedR):
            return False
        if not is_prime(truncatedL):
            return False
    return True

count = 0
s = 0
primes = primes_from_2_to(10**6)[4:]
for prime in primes:
    if truncatable(prime):
        s += prime
print(s)
