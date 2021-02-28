import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0 and heap:
        print(heapq.heappop(heap))
    elif x == 0 and not heap:
        print(0)
    else:
        heapq.heappush(heap, x)