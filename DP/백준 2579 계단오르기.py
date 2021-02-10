TC = int(input())
lst = [0 for _ in range(301)]
dp = [0 for _ in range(301)]
for i in range(TC):
    lst[i] = int(input())
dp[0] = lst[0]
dp[1] = lst[0] + lst[1]
dp[2] = max(lst[0] + lst[2], lst[1] + lst[2])

for i in range(3, TC):
    dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i])

print(dp[TC-1])