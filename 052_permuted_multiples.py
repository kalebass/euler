for m in range(6, 8):
    for x in range(10**m + 8, int(10/6 * 10**m), 9):
        digits = set(str(x))
        for factor in range(1, 7):
            if set(str(factor * x)) != digits:
                break
        else:
            print(x)
            raise SystemExit
