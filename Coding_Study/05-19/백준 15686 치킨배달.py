from itertools import combinations
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

minV = float('inf')
for ch in combinations(chicken, M):
    sumvV= 0
    for home in house:
        result = []
        for i in ch:
            result.append(abs(home[0] - i[0]) + abs(home[1] - i[1]))
        sumvV += min(result)
        if minV <= sumvV:
            break
    if sumvV < minV:
        minV = sumvV

print(minV)
