from euler import is_prime, primes_from_2_to

def is_circular(prime: int) -> bool:
    pstr = str(prime)
    for shift in range(1, len(pstr)):
        shifted = int(pstr[shift:] + pstr[:shift])
        if not is_prime(shifted):
            return False
    return True

prime_list = primes_from_2_to(1000000)
circular = [prime for prime in prime_list if is_circular(prime)]
print(len(circular))
