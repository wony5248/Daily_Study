import sys
from collections import deque

result = 0
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
N, M = map(int, sys.stdin.readline().split())
lab = []

for i in range(N):
    lab.append(list(map(int, sys.stdin.readline().split())))


def wall(wallnum):
    if wallnum == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(wallnum+1)
                lab[i][j] = 0


def bfs():
    global result
    lab1 = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            lab1[i][j] = lab[i][j]
    count = 0
    for i in range(N):
        for j in range(M):
            if lab1[i][j] == 2:
                queue.append([i, j])
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and lab1[nx][ny] == 0:
                lab1[nx][ny] = 2
                queue.append([nx, ny])
    for i in range(N):
        for j in range(M):
            if lab1[i][j] == 0:
                count += 1
    result = max(result, count)


queue = deque()


wall(0)
print(result)
