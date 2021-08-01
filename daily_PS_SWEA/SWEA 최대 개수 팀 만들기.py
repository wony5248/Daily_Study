from collections import deque
import copy
import sys

def bfs(x, y):
    queue = deque()
    queue. append([x, y])
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] >= 1 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx, ny])


def score():
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 1:
                graph[i][j] -= 1

TC = int(input())
for t in range(TC):
    N = int(input())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    yearnum = 0

    for i in range(N):
        graph[i] = list(map(int, sys.stdin.readline().split()))


    while True:
        score()
        count = 0
        visit = [[0 for _ in range(N)] for _ in range(N)]
        for j in range(N):
            for k in range(N):
                if graph[j][k] >= 1 and visit[j][k] == 0:
                    bfs(j, k)
                    count += 1
        result.append(count)
        if count == 0:
            break
    if max(result) == 0:
        result.append(1)

    print("#%d %d"%(t+1, max(result)))
