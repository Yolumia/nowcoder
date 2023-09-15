def maxCoinValue(coins):
    n = len(coins)
    if n == 0:
        return 0
    if n == 1:
        return coins[0]

    dp = [0] * (n + 1)
    dp[1] = coins[0]

    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + coins[i - 1])

    return dp[n]

# 读取输入
coins = list(map(int, input().split()))
result = maxCoinValue(coins)
print(result)