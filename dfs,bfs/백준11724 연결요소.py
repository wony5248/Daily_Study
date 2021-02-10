from collections import deque
import sys
sys.setrecursionlimit(10000)



N, M = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
count = 0
def dfs(x):
    visit[x] = 1
    for k in range(1, N+1):
        if graph[x][k] == 1 and visit[k]==0:
            dfs(k)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = graph[v][u] = 1

for i in range(1,N+1):
    if visit[i] ==0:
        dfs(i)
        count += 1
print(count)
