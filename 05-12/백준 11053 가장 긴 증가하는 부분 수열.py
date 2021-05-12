N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):              # 자기 자신보다 작은수 다 탐색
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j])           
    dp[i] += 1             # 자기 자신 추가


print(max(dp))