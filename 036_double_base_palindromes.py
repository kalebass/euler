def palindromic(string: str) -> bool:
    return string == string[::-1]

print(sum(n for n in range(1000000) if palindromic(format(n, 'b')) and palindromic(str(n))))
