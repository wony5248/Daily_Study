from itertools import permutations
import sys
import copy
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = [list(map(int, input().split())) for _ in range(K)]
origin = copy.deepcopy(arr)
perm = list(permutations(lst, len(lst)))
minV = float("inf")
for i in perm:
    cnt = float("inf")
    arr2 = copy.deepcopy(arr)
    for r, c, s in i:
        for j in range(s):
            for k in range(j, (s*2)-j):
                arr[r-s+j-1][c-s+k] = arr2[r-s+j-1][c-s-1+k]
                arr[r+s-j-1][c-s-1+k] = arr2[r+s-j-1][c-s+k]
        for j in range(s):
            for k in range(j, (s*2)-j):
                arr[r-s+k-1][c-s+j-1] = arr2[r-s+k][c-s+j-1]
                arr[r-s+k][c+s-j-1] = arr2[r-s+k-1][c+s-j-1]
        arr2 = copy.deepcopy(arr)
    for j in range(N):
        cnt = min(cnt, sum(arr2[j]))
    minV = min(minV, cnt)
    arr = copy.deepcopy(origin)

print(minV)

