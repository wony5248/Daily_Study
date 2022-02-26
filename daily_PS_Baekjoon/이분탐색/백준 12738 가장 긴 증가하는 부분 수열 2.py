import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = [0]

for i in A:
    if dp[-1] < i:
        dp.append(i)
    else:
        dp[bisect_left(dp, i)] = i


print(len(dp) - 1)
