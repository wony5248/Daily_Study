from collections import deque
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
result = [[0 for _ in range(M)] for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
miro = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def bfs(x, y):                    # 0,0 부터 bfs 탐색 시작
    queue = deque()
    queue.append([x, y])
    result[x][y] = 1
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]      # 상하좌우 4방향 탐색
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1 and visit[nx][ny] == 0:
                queue.append([nx,ny])          # 방문하지 않았고 이동할수 있는 칸이고 미로영역 안 일경우
                visit[nx][ny] = 1              # 방문 표시
                result[nx][ny] = result[cx][cy] + 1   # 다음 지점까지의 칸수 = 현재까지의 칸수 + 1



bfs(0, 0)
print(result[N-1][M-1])