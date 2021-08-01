import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
result = set(permutations(lst, M))
result = list(result)
result.sort()

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=" ")
    print()