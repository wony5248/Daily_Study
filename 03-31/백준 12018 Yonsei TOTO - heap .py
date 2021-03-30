import sys
import heapq
input = sys.stdin.readline
count = 0

n, m = map(int, input().split())
result = []
for i in range(n):
    P, L = map(int, input().split())
    mile = list(map(int, input().split()))
    heapq.heapify(mile)
    if P > L:
        for j in range(P - L + 1):
            x = heapq.heappop(mile)
        result.append(x)

    else:
        result.append(1)

result.sort()
for i in result:
    if i <= m:
        count += 1
        m -= i
# print(result)
print(count)