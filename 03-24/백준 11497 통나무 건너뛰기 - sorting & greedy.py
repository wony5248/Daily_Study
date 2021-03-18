import heapq
T = int(input())
for _ in range(T):
    N = int(input())
    result = 100000
    L = list(map(int, input().split()))
    heapq.heapify(L)
    

