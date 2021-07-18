n, t = map(int, input().split())    # 단원수, 공부 시간
time = []
score = []
dp = [[0 for _ in range(t+1)] for _ in range(n+1)]
for i in range(n):
    k, s = map(int, input().split())     # 예상공부시간, 배점
    time.append(k)
    score.append(s)

for i in range(1, n+1):
    for j in range(1, t+1):
        if j >= time[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i-1]] + score[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][t])