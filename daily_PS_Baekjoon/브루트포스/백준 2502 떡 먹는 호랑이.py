D, K = map(int, input().split())
isflag = 1
dp = [0 for _ in range(D)]
first = 1
second = 1
while isflag:
    dp[0] = first
    dp[1] = second
    for i in range(2, D):
        dp[i] = dp[i-1] + dp[i-2]
    if dp[D-1] == K:
        isflag = 0
    elif dp[D-1] < K:
        second += 1
    elif dp[D-1] > K:
        second = 1
        first += 1

print(first)
print(second)

