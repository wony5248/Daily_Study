import sys
from collections import deque
N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

time = 0
result = []
def bfs():
    visit = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append([0, 0])
    cnt = 0
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0 and cheese[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx, ny])
            elif 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0 and cheese[nx][ny] == 1:
                visit[nx][ny] = 1
                cheese[nx][ny] = 0
                cnt += 1
    if cnt != 0:
        result.append(cnt)
    return cnt



while True:
    x = bfs()
    if x == 0:
        break
    time += 1
print(time)
print(result[-1])