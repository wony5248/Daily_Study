from itertools import combinations
import sys
input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
lst = set([(i+1) for i in range(N)])
comb = set(combinations(lst, len(lst) // 2))
minV = float("inf")
result = set()
for i in comb:
    left = 0
    right = 0
    result.add(set(i))
    lst2 = lst - set(i)
    if lst2 not in result:

        for j in i:
            for k in i:
                if j != k:
                    left += S[k-1][j-1]

        for j in lst2:
            for k in lst2:
                if j != k:
                    right += S[k-1][j-1]

        if minV > abs(left - right):
            minV = abs(left - right)

print(minV)