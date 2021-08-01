from collections import deque
N, M = map(int, input().split())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
result = [[0 for _ in range(M)] for _ in range(N)]
miro = [[0 for _ in range(M)] for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    result[x][y] = 1
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1 and visit[nx][ny] == 0:
                queue.append([nx,ny])
                visit[nx][ny] = 1
                result[nx][ny] = result[cx][cy] + 1

for i in range(N):
    miro[i] = list(map(int, input()))

bfs(0, 0)


print(result[N-1][M-1])