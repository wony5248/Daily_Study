import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
heap = list(map(int, sys.stdin.readline().split()))
heapq.heapify(heap)
for i in range(m):
    sumV = heapq.heappop(heap) + heapq.heappop(heap) # 제일 작은수 두개 빼서 더해줌
    heapq.heappush(heap, sumV)                  # 더해준 수를 두개 추가  -> 합친 수로 바꿔주는 작업
    heapq.heappush(heap, sumV)

print(sum(heap))