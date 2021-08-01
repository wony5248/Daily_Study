import sys
from itertools import combinations
N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
count = 0
result = []
for i in range(1, N+1):
    com = list(combinations(lst, i))
    for j in com:
        result.append(j)
for i in range(len(result)):
    if sum(result[i]) == S:
        count += 1

print(count)