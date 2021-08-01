import heapq
import sys
input = sys.stdin.readline
N = int(input())
mheap = []
count = 0
x = [int(input()) for i in range(N)]
for i in x:
    if i == 0:
        if mheap:
            x, y = heapq.heappop(mheap)
            print(y)
        else:
            print(0)
    else:
        heapq.heappush(mheap, (abs(i), i))         # 튜플로 넣어줄 시 맨 앞 값만 가지고 순서 정함

