import itertools
from typing import Generator

digits = '0123456789'
def special() -> Generator[int, None, None]:
    for num in itertools.permutations(digits):
        num = ''.join(num)
        if not(int(num[1:4]) % 2 or
        int(num[2:5]) % 3 or
        int(num[3:6]) % 5 or
        int(num[4:7]) % 7 or
        int(num[5:8]) % 11 or
        int(num[6:9]) % 13 or
        int(num[7:10]) % 17):
            yield int(num)

print(sum(special()))
