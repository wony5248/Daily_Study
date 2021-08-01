import sys
from collections import deque
N, M = map(int, sys.stdin.readline().rstrip().split())
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
mountain = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]

result = 0
def bfs(x,y):
    isflag = 0                          # 주변에 자기보다 높은게 있는지 없는지 확인용
    global result
    queue = deque()
    queue.append([x, y])
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(8):
            nx = cx + dx[d]
            ny = cy + dy[d]
            # 범위 내에 있고 방문하지 않았고, 지금 내 높이랑 같다면
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0 and mountain[nx][ny] == mountain[cx][cy]:
                queue.append([nx, ny])    # 탐색
                visit[nx][ny] = 1         # 방문 표시
            if 0 <= nx < N and 0 <= ny < M and mountain[nx][ny] > mountain[cx][cy]:
                # 범위내에 있는 내 인접 격자 중에 자기 보다 높은 산봉우리가 있다면
                isflag = 1
    if isflag == 0:
        result += 1

for i in range(N):
    for j in range(M):
        if visit[i][j] == 0:
            bfs(i, j)

print(result)