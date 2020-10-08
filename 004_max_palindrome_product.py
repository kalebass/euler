from typing import Union

def p004() -> Union[int, None]:
    for n in range(999, 899, -1):
        n_reverse = 100 * (n % 10) + 10 * ((n // 10) % 10) + 9
        palindrome = 1000*n + n_reverse
        for divisor in range(999, int(palindrome / 1000), -1):
            if palindrome % divisor == 0:
                return palindrome

print(p004())
