n, m = map(int, input().split())
dp = [1 for _ in range(n+1)]
dp[1] = 1
for i in range(2, n+1):
    dp[i] = i * dp[i-1]
print(dp[n] // (dp[m] * dp[n - m]))


