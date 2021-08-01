import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
guide = [list(input().rstrip()) for _ in range(N)]
result = 0

def bfs(x, y):
    global result
    visit = [[0 for _ in range(M)] for _ in range(N)]
    check = [[0 for _ in range(M)] for _ in range(N)]
    cnt = []

    queue = deque()
    queue.append([x, y])
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M and guide[nx][ny] == "L" and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                check[nx][ny] = check[cx][cy] + 1
                cnt.append(check[nx][ny])          # 한 육지당 모든 육지까지의 최단거리 cnt에 다 넣어줌
                queue.append([nx, ny])              
    if cnt and result < max(cnt):        # 해당 육지에서 가장 먼 육지까지의 거리랑 result 비교후 더크면 result 바꿔줌
        result = max(cnt)


for i in range(N):
    for j in range(M):             # 모든 육지를 출발점으로 완전탐색
        if guide[i][j] == "L":
            bfs(i, j)
print(result)











