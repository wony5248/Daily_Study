from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


N, M = map(int, input().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
picture = [0,]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visit[x][y] = 1
    picture.append(1)
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and visit[nx][ny] == 0:
                queue.append([nx, ny])
                visit[nx][ny] = 1
                picture[-1] += 1


for i in range(N):
    graph[i] = list(map(int, input().split()))

count = 0
for j in range(N):
    for k in range(M):
        if graph[j][k] == 1 and visit[j][k] == 0:
            bfs(j, k)
            count += 1


print(count)
print(max(picture))
