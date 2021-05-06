N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1


print(max(dp))