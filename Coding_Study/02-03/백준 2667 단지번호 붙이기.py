from collections import deque
N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
house = []
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
count = 0
def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visit[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx, ny])
                house[count-1] += 1

for i in range(N):
    graph[i] = list(map(int, input()))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visit[i][j] == 0:
            count += 1
            house.append(1)
            bfs(i, j)
print(count)
house.sort()
for i in range(count):
    print(house[i])



