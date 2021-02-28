import heapq
import sys


N = int(sys.stdin.readline())          # input에서 시간초과  -> 바꾸고 통과
heap = []
for j in range(N):
     x = int(sys.stdin.readline())
     if x == 0:
         if not heap:
             print(0)
         else:
             print((heapq.heappop(heap)) * -1)
     else:
         heapq.heappush(heap, -x)





