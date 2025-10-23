def coin_changes_ways(S : int, coins: list[int]) -> int:
    dp = [0] *(S + 1)
    dp[0] = 1
    for coin in coins:
        for amount in range(coin, S + 1):
            dp[amount] += dp[amount - coin]
    return dp[S]

S_example = 10
coins_example = [2,3,5]
result_ways = coin_changes_ways(S_example, coins_example)
print(f"So tien can doi: {S_example}")
print(f"Menh gia: {coins_example}")
print(f"So cach khac nhau de doi tien: {result_ways}")
