from collections import deque
import copy
import sys
N, M = map(int, sys.stdin.readline().split())
area = [[0 for _ in range(M)] for _ in range(N)]
area1 = [[0 for _ in range(M)] for _ in range(N)]
graph = [[0 for _ in range(M)] for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
yearnum = 0

def bfs(x, y):
    queue = deque()
    queue. append([x, y])
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M and area[nx][ny] >= 1 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx, ny])


def year():
    global yearnum
    yearnum += 1
    for i in range(N):
        for j in range(M):
            if area1[i][j] >= 1:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and area1[nx][ny] == 0:
                        area[i][j] -= 1
                        if area[i][j] == 0:
                            break
    for i in range(N):
        for j in range(M):
            area1[i][j] = area[i][j]


for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))

area = copy.deepcopy(graph)
area1 = copy.deepcopy(graph)


while True:
    year()
    count = 0
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(N):
        for k in range(M):
            if area[j][k] >= 1 and visit[j][k] == 0:
                bfs(j, k)
                count += 1
    if count >= 2:
        break
    elif count == 0:
        yearnum = 0
        break


print(yearnum)
