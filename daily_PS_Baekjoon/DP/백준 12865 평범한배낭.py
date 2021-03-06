import sys
input = sys.stdin.readline

N, K = map(int, input().split())
item = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]


for i in range(1, N+1):
    for j in range(1, K+1):
        W = item[i][0]
        V = item[i][1]
        if j < W:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(V + dp[i - 1][j - W], dp[i - 1][j])

print(dp[N][K])