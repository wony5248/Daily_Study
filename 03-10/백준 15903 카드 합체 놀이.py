import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
heap = list(map(int, sys.stdin.readline().split()))
heapq.heapify(heap)
for i in range(m):
    sumV = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, sumV)
    heapq.heappush(heap, sumV)

print(sum(heap))