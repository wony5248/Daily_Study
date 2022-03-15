import sys
import math
from functools import reduce
input = sys.stdin.readline

N = int(input().rstrip())
S = []

def multiply(arrs):
    return reduce(lambda x, y: x * y, arrs)

def lcm(arrs):
    return multiply(arrs) // math.gcd(*arrs)

for _ in range(N):
    S.append(input().rstrip()[2:])

d = {}
for i in range(1, 954):
    for j in range(i):
        t = f'{j/i:.4f}'[2:5]
        if t not in d:
            d[t] = i

ans = []
for v in S:
    ans.append(d[v])




print(lcm(ans))