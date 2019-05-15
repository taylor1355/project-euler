def num_ways(amount, coins):
    new_coins = list(coins)
    curr_coin = new_coins[0]
    del new_coins[0]
    if len(new_coins) == 0:
        if amount % curr_coin == 0:
            return 1
        else:
            return 0

    ways = 0
    for i in range(0, amount // curr_coin + 1):
        new_amount = amount - curr_coin * i
        ways += num_ways(new_amount, new_coins)
    return ways

coins = [200, 100, 50, 20, 10, 5, 2, 1]
amount = 200
print(num_ways(amount, coins), "ways to make change")
