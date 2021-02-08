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
            if 0 <= nx < N and 0 <= ny < N and area[nx][ny] >= 1 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx, ny])


def score():
    global yearnum
    yearnum += 1
    for i in range(N):
        for j in range(N):
            if area1[i][j] >= 1:
                area[i][j] -= 1
    for i in range(N):
        for j in range(N):
            area1[i][j] = area[i][j]


N = int(input())
area = [[0 for _ in range(N)] for _ in range(N)]
area1 = [[0 for _ in range(N)] for _ in range(N)]
graph = [[0 for _ in range(N)] for _ in range(N)]
result = []
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
yearnum = 0


for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))

area = copy.deepcopy(graph)
area1 = copy.deepcopy(graph)


while True:
    score()
    count = 0
    visit = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if area[j][k] >= 1 and visit[j][k] == 0:
                bfs(j, k)
                count += 1
    result.append(count)
    if count == 0:
        yearnum = 0
        break


print(max(result))
