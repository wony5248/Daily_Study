import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = [-1000000001]
sp = [-1000000001]
for i in A:
    x = bisect_left(dp, i)
    y = bisect_right(dp, i)
    print(i)
    print(x)
    print(y)
    if dp[-1] < i:
        dp.append(i)
        sp.append(i)
    else:

        dp[x] = i
        sp[y] = i
    print(dp)
    print(sp)


print(len(dp) - 1)