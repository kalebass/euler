def dcham(n: int) -> int:
    digits = 0
    alld = 0
    while n > alld:
        n -= alld
        alld = 9 * 10**digits * (digits + 1)
        digits += 1
    subnums = (n - 1) // digits
    subpos = -n % digits
    cursub = 10**(digits - 1) + subnums
    res = (cursub // 10**subpos) % 10
    return res

product = 1
for k in range(7):
    product *= dcham(10**k)
print(product)
