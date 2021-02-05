N = int(input())
day = []
price = []
dp = []
for i in range(N):
    T, P = map(int, input().split())
    day.append(T)
    price.append(P)
    dp.append(P)
dp.append(0)
for i in range(N-1, -1, -1):
    if day[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], price[i] + dp[i+day[i]])
print(dp[0])