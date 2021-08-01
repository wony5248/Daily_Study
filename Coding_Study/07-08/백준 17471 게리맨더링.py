import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
people = list(map(int, input().split()))
allcity = set(i for i in range(N))


def bfs(city):
    queue = deque()
    visit = [0 for _ in range(N)]
    queue.append(city[0])
    visit[city[0]] = 1
    sumV = 0
    while queue:
        cx = queue.popleft()
        sumV += people[cx]
        for d in range(N):
            if graph[cx][d] != 0 and d in city and visit[d] == 0:
                queue.append(d)
                visit[d] = 1
    return sumV, visit.count(1)


for i in range(N):
    connect = list(map(int, input().split()))
    for j in range(1, len(connect)):
        graph[i][connect[j] - 1] = 1


minV = 1001
for i in range(1, N//2 + 1):
    comb = list(combinations(allcity, i))
    print(comb)
    for city1 in comb:
        city1 = set(city1)
        city2 = allcity - city1
        sum1, con1 = bfs(list(city1))
        sum2, con2 = bfs(list(city2))
        if con1 + con2 == N:
            minV = min(minV, abs(sum1 - sum2))


if minV == 1001:
    print(-1)
else:
    print(minV)



