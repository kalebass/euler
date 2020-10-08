def combinations(target: int, coins: tuple[int, ...]) -> int:
    if coins == (1,):
        return 1
    count = 0
    for i in range(len(coins)):
        if coins[i] < target:
            count += combinations(target - coins[i], coins[i:])
        elif coins[i] == target:
            count += 1
    return count

coins = 200, 100, 50, 20, 10, 5, 2, 1
print(combinations(200, coins))
