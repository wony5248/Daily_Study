T = int(input())
for tc in range(T):
    day, month, month3, year = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0 for _ in range(len(plan))]
    result = 0
    dp[0] = min(month, day * plan[0])
    dp[1] = min(dp[0] + month, dp[0] + day * plan[1])
    dp[2] = min(min(dp[1] + month, dp[1] + day * plan[2]), min(dp[1] + month, month3))
    for i in range(3, len(plan)):
        dp[i] = min(min(dp[i-1] + month, dp[i-1] + day * plan[i]), min(dp[i-1] + month, dp[i-3] + month3))
    if dp[-1] > year:
        print("#%d %d" %(tc+1, year))
    else:
        print("#%d %d" %(tc+1, dp[-1]))

