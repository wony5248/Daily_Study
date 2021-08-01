from collections import deque
N = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
queue = deque()
maxcount = 0
def bfs(x, y):
    queue. append([x, y])
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and area[nx][ny] >= 1 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx, ny])
for i in range(N):
    graph[i] = list(map(int, input().split()))
for i in range(101):
    area = [[0 for _ in range(N)] for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    count = 0
    for j in range(N):
        for k in range(N):
            area[j][k] = graph[j][k] - i

    for j in range(N):
        for k in range(N):
            if area[j][k] >= 1 and visit[j][k] == 0:
                bfs(j, k)
                count += 1
    if count == 0:
        break
    maxcount = max(maxcount, count)
print(maxcount)
