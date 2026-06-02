coins = [1,2,5]
amount = 11

def coinChange(coins, amount):
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    min_coins = float('inf')
    for coin in coins:
        check = coinChange(coins, amount - coin)
        if check >= 0 and check < min_coins:
            min_coins = 1 + check