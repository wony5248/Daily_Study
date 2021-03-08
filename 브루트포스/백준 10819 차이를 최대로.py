import sys
from itertools import permutations, combinations
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
all = list(permutations(lst, N))
result = []
for i in range(len(all)):
    maxV = 0
    for j in range(N-1):
        maxV += abs(all[i][j] - all[i][j+1])
    result.append(maxV)
print(max(result))