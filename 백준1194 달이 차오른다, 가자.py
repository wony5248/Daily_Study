import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
miro = [list(input().rstrip()) for _ in range(N)]
key = [[[0 for _ in range(64)] for _ in range(M)] for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]



def bfs(x, y):
    queue = deque()
    queue.append([x, y, 0])
    key[x][y][0] = 1
    while queue:
        cx, cy, cz = queue.popleft()
        if miro[cx][cy] == "1":
            print(key[cx][cy][cz] - 1)
            return
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] != "#" and key[nx][ny][cz] == 0:
                if miro[nx][ny].islower():
                    nz = cz | (1 << (ord(miro[nx][ny]) - ord("a")))
                    if key[nx][ny][nz] == 0:
                        key[nx][ny][nz] = key[cx][cy][cz] + 1
                        queue.append([nx, ny, nz])
                elif miro[nx][ny].isupper():
                    if cz & (1 << (ord(miro[nx][ny]) - ord("A"))):
                        key[nx][ny][cz] = key[cx][cy][cz] + 1
                        queue.append([nx, ny, cz])
                else:
                    key[nx][ny][cz] = key[cx][cy][cz] + 1
                    queue.append([nx, ny, cz])
    print(-1)




for i in range(N):
    for j in range(M):
        if miro[i][j] == "0":
            bfs(i, j)

