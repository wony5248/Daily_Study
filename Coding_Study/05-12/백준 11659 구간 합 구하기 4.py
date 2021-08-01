import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = lst[0]
for i in range(1, N):
    dp[i] = lst[i] + dp[i-1]

for i in range(M):
    x, y = map(int, input().split())
    if x == 1:
        print(dp[y-1])
    else:
        print(dp[y-1] - dp[x-2])