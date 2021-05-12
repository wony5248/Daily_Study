import sys
input = sys.stdin.readline

N, K = map(int, input().split())
item = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]


for i in range(1, N+1):           # 가방의 무게
    for j in range(1, K+1):       
        W = item[i][0]            # 무게
        V = item[i][1]            # 가치
        if j < W:           # 지금꺼를 배낭에 못 담는다면
            dp[i][j] = dp[i - 1][j]   # 지금까지의 최댓값
        else:
            # 지금꺼 담고 지금까지의 최댓값 더한거 vs 전꺼에 지금꺼 안 더한 것중 최댓값
            dp[i][j] = max(V + dp[i - 1][j - W], dp[i - 1][j])

print(dp[N][K])