N = int(input())
dp = [1 for _ in range(N)]
A = list(map(int, input().split()))
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
maxV = max(dp)
lst = []
for i in range(N-1, -1, -1):
    if dp[i] == maxV:
        lst.append(A[i])
        maxV -= 1
lst.reverse()
print(*lst)