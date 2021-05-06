import sys
import heapq
input = sys.stdin.readline

T = int(input())
for i in range(T):
    k = int(input())
    minheap = []
    maxheap = []
    heap = []
    for j in range(k):
        com = list(input().split())
        if com[0] == "I":
            heapq.heappush(minheap, int(com[1]))
            heapq.heappush(maxheap, int(com[1]) * -1)
        elif com[0] == "D" and com[1] == "-1" and minheap:
            heapq.heappop(minheap)
        elif com[0] == "D" and com[1] == "1" and maxheap:
            heapq.heappop(maxheap)
        print(minheap)
        print(maxheap)
        print()

    for j in range(len(maxheap)):
        maxheap[j] = maxheap[j] * -1
    minheap = set(minheap)

    maxheap = set(maxheap)

    heap = minheap & maxheap
    if not heap:
        print("EMPTY")
    else:
        heap = list(heap)
        heap.sort()
        print("%d %d" %(heap[-1], heap[0]))



