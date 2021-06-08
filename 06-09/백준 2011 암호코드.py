import sys
input = sys.stdin.readline
secret = list(input().rstrip())
# print(secret)
dp = [0 for _ in range(len(secret) + 1)]
dp[0] = 1
dp[1] = 1
if secret[0] == "0":
    print(0)
else:
    for i in range(2, len(secret) + 1):
        if int(secret[i-1]) > 0:
            dp[i] += dp[i-1]
        if 10 <= int(secret[i-2] + secret[i-1]) <= 26:
            dp[i] += dp[i-2]
# print(dp)
    print(dp[-1] % 1000000)

