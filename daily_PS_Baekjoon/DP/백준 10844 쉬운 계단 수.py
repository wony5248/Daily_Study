n = int(input())
dp = [[0 for i in range(10)] for j in range(101)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = (dp[i - 1][1]) % 1000000000
        elif j == 9:
            dp[i][j] = (dp[i - 1][8]) % 1000000000
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000
print(sum(dp[n]) % 1000000000)