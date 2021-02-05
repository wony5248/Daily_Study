from collections import deque

N, M, K = map(int, input().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
result = []
dx = [0, -1, 0 ,1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    count = 0
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and visit[nx][ny] ==0:
                visit[nx][ny] = 1
                queue.append([nx, ny])
                count += 1
    result.append(count)


for i in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

for j in range(N):
    for k in range(M):
        if graph[j][k] == 1:
            bfs(j, k)
print(max(result))