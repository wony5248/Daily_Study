import sys
from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

result = []
isflag = 0

def bfs(x, y):
    global count
    global isflag
    queue = deque()
    queue.append([x, y, 1])
    visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visit[x][y][1] = 1
    while queue:
        cx, cy, cw = queue.popleft()
        if cx == N-1 and cy == M-1:
            return visit[cx][cy][cw]
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if MAP[nx][ny] == 1 and cw ==1:
                    visit[nx][ny][0] = visit[cx][cy][1] + 1
                    queue.append([nx, ny, 0])
                elif MAP[nx][ny] == 0 and visit[nx][ny][cw] == 0:
                    visit[nx][ny][cw] = visit[cx][cy][cw] + 1
                    queue.append([nx,ny,cw])
    return - 1
print(bfs(0,0))        # 다  0일수도 있음
