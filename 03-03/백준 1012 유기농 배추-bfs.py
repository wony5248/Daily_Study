from collections import deque
T = int(input())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]     # 좌 상 우 하 탐색
def bfs(startx, starty):
    queue = deque()
    queue.append([startx, starty])
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny <M and visit[nx][ny] == 0 and farm[nx][ny] == 1:   # 전체 크기안에 있고 방문하지 않았고 배추가 심어져 있다면 방문
                visit[nx][ny] = 1                          # 방문했다고 표시
                queue.append([nx, ny])                     # 방문


for i in range(T):
    M, N, K = map(int, input().split())
    farm = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    for j in range(K):
        y, x = map(int, input().split())         
        farm[x][y] = 1                                  # 배추 심은 위치는 1로 초기화
    for j in range(N):
        for k in range(M):
            if farm[j][k] == 1 and visit[j][k] == 0:    # 배추가 심어져 있고 방문하지 않았다면
                bfs(j, k)                               # 그 위치 부터 탐색 -> 좌우 상하 붙어있는 구역 다 탐색
                count += 1                              # 영역수 1 증가
    print(count)