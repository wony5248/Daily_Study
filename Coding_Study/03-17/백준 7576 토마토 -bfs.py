import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
queue = deque()
count = 0
isflag = 0
def bfs():
    while queue:
        cx, cy = queue.popleft()    # 토마토 위치 꺼내주고
        for d in range(4):
            nx = cx + dx[d]        # 상하좌우 탐색
            ny = cy + dy[d]
            # farm 내부이고 방문 안했고, 익지 않은 토마토라면
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0 and farm[nx][ny] >= 0:
                farm[nx][ny] = farm[cx][cy] + 1   # 현재 까지의 일수 + 1해줌
                visit[nx][ny] = 1         #   방문 표시
                queue.append([nx, ny])    # 방문




for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            queue.append([i, j])    # 토마토가 있는 위치 다 deque에 넣어줌
            visit[i][j] = 1

bfs()

for i in range(N):
    for j in range(M):
        if farm[i][j] > count:
            count = farm[i][j]      # count는 해당 농장에서 가장 마지막 토마토가 익는데 걸린 시간
        if farm[i][j] == 0:
            isflag = 1       # 탐색 다 끝났는데 익지 않은 토마토가 있다면
if isflag == 1:
    print("-1")
else:
    print(count - 1)   # 초기값이 1에서 시작이므로 -1 해줌
