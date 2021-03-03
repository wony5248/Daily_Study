import sys
import heapq
N, M = map(int, sys.stdin.readline().split())
result = []
heap = []
for i in range(N):
    num = int(sys.stdin.readline())
    result.append(num)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(min(result[a-1:b]), end=" ")
    print(max(result[a-1:b]))