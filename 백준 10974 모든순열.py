import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
lst = list()
for i in range(1, N+1):
    lst.append(i)
for i in range(1, N+1):
    per = list(permutations(lst, i))
per.sort()
for i in range(len(per)):
    for j in range(N):
        print(per[i][j] ,end=" ")
    print()