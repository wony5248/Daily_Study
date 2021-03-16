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
    queue.append([x, y])
    visit = [[0 for _ in range(M)] for _ in range(N)]
    check = [[1 for _ in range(M)] for _ in range(N)]
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        if cx == N-1 and cy == M-1:
            isflag = 1
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0 and MAP[nx][ny] == 0:
                visit[nx][ny] = 1
                check[nx][ny] = check[cx][cy] + 1
                queue.append([nx, ny])
    if check[N-1][M-1] != 1:
        result.append(check[N-1][M-1])
bfs(0, 0)        # 다  0일수도 있음
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1 and (MAP[i-1][j] ==0 or MAP[i-1][j] ==0 and MAP[i-1][j] ==0):
            MAP[i][j] = 0
            bfs(0, 0)
            MAP[i][j] = 1
if isflag == 0:
    print("-1")
else:
    print(min(result))