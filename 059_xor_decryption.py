import csv
from typing import Generator

with open('p059_cipher.txt') as csvfile:
    reader = csv.reader(csvfile)
    ascii_list = next(reader)

def to_ints() -> Generator[int, None, None]:
    for string in ascii_list:
        yield int(string)

binary = bytearray(to_ints())

with open('p059_bytes.txt', 'wb') as outfile:
    outfile.write(binary)
