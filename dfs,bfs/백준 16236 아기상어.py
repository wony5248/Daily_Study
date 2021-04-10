from collections import deque
N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
size = 2
eat = 0
result = 0
def bfs(x, y):
    global count
    count = []
    global size
    visit = [[0 for _ in range(N)] for _ in range(N)]

    check = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append([x, y])
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and space[nx][ny] <= size:
                if space[nx][ny] == 0 or space[nx][ny] <= size:
                    queue.append([nx, ny])
                    visit[nx][ny] = 1
                    check[nx][ny] = check[cx][cy] + 1
                if 0 < space[nx][ny] < size:
                    check[nx][ny] = check[cx][cy] + 1
                    count.append([nx, ny, check[nx][ny]])


for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            bfs(i, j)
            space[i][j] = 0

while True:
    if not count:
        break
    count.sort(key= lambda x: (x[2], x[0], x[1]))
    rx, ry, dist = count[0][0], count[0][1], count[0][2]
    space[rx][ry] = 0
    result += dist
    eat += 1
    if eat == size:
        size += 1
        eat = 0
    bfs(rx, ry)
print(result)




