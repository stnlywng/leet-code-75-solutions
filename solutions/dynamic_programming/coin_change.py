from typing import List

# coin change TWO not one!
def coin_change_sol(amount: int, coins: List[int]) -> int:
    size = amount + 1
    dp = [0] * size
    dp[0] = 1

    for i, coin in enumerate(coins):
        for index in range(coin, size):
            dp[index] += dp[index - coin]

    print(dp[amount])

    return dp[amount]