import sys
import heapq
heap = []
K, N = map(int, input().split())
for i in range(K):
    x = int(input())

    heapq.heappush(heap, (-1)*x)


while N > -1:
    maxV = (-1) * heapq.heappop(heap)
    maxV = maxV // 2
    print(maxV)
    heapq.heappush(heap, (-1)*maxV)
    N -= 2

print(heap)