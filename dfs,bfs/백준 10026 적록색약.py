from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
N = int(input())
normal = [[0 for _ in range(N)] for _ in range(N)]
color = [[0 for _ in range(N)] for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
visit1 = [[0 for _ in range(N)] for _ in range(N)]
queue = deque()
queue1 = deque()
count = 0
count1 = 0

def bfs1(x, y):
    queue.append([x, y])
    visit1[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and color[nx][ny] == color[cx][cy] and visit1[nx][ny] == 0:
                visit1[nx][ny] = 1
                queue.append([nx, ny])
def bfs(x, y):
    queue.append([x, y])
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and normal[nx][ny] == normal[cx][cy] and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx, ny])



for i in range(N):
    normal[i] = list(input())
for i in range(N):
    for j in range(N):
        if normal[i][j] == "G":
            color[i][j] = "R"
        else:
            color[i][j] = normal[i][j]


for i in range(N):
    for j in range(N):
        if normal[i][j] and visit[i][j] == 0:
            bfs(i, j)
            count += 1
for i in range(N):
    for j in range(N):
        if color[i][j] and visit1[i][j] == 0:
            bfs1(i, j)
            count1 += 1

print(count)
print(count1)
