n = int(input())
cnt = 0
dp = [0 for _ in range(50001)]
dp[1] = 1
dp[2] = 2
for i in range(1, n+1):
    dp[i] = dp[1] + dp[i-1]             # 1 의제곱으로 더해준걸 base로하고
    for j in range(2, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], 1 + dp[i - j**2])    # i보다 작은 모든 j**2 전에서 + 1 해준거랑 비교

print(dp[n])


