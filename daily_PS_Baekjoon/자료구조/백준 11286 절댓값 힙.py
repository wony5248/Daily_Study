import heapq
import sys
N = int(sys.stdin.readline())
mheap = []
count = 0
x = [int(sys.stdin.readline()) for i in range(N)]
for i in x:
    if i == 0:
        if mheap:
            x, y = heapq.heappop(mheap)
            print(y)
        else:
            print(0)
    else:
        heapq.heappush(mheap, (abs(i), i))

