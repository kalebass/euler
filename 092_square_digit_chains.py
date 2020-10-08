def ends_at_one(n: int) -> bool:
    if n == 1:
        return True
    if n == 89:
        return False
    return ends_at_one(sum(int(d) * int(d) for d in str(n)))
