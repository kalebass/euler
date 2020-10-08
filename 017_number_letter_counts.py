singles = '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
teens = 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
nties = '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'

def letter(n: int) -> str:
    digits = [int(d) for d in str(n).zfill(3)]
    res: list[str] = []
    if digits[-3] > 0:
        res.append(singles[digits[-3]])
        res.append('hundred')
        if n % 100 > 0:
            res.append('and')
    if digits[-2] >= 2:
        res.append(nties[digits[-2]])
    if digits[-2] == 1:
        res.append(teens[digits[-1]])
    else:
        res.append(singles[digits[-1]])
    return ''.join(res)

print(sum(len(letter(number)) for number in range(1, 1000)))
