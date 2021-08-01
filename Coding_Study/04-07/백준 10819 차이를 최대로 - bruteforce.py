import sys
from itertools import permutations, combinations
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
all = list(permutations(lst, N))                             # N자리 모든 순열 뽑아서
result = []
for i in range(len(all)):
    maxV = 0
    for j in range(N-1):
        maxV += abs(all[i][j] - all[i][j+1])                  # 다 돌면서 탐색
    result.append(maxV)
print(max(result))