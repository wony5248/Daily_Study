import sys
input = sys.stdin.readline
N, D = map(int, input().split())
dp = [i for i in range(D+1)]
road = [list(map(int, input().split())) for _ in range(N)]
for i in range(D+1):
    if i > 0:
        dp[i] = min(dp[i-1] + 1, dp[i])
    for j in range(len(road)):
        if road[j][0] == i and road[j][0] <= D and road[j][1] <= D:
            dp[road[j][1]] = min(dp[road[j][1]], dp[i] + road[j][2])



print(dp[D])