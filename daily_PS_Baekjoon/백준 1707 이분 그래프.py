from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
R, C = map(int, input().split())
farm = [list(input()) for _ in range(R)]
visit = [[0 for _ in range(C)] for _ in range(R)]
wolf = 0
sheep = 0
def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visit[x][y] = 1
    global sheep
    global wolf
    wo = 0
    sh = 0
    while queue:
        cx, cy = queue.popleft()
        if farm[cx][cy] == "v":
            wo += 1
        elif farm[cx][cy] == "o":
            sh += 1
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < R and 0 <= ny < C and visit[nx][ny] == 0 and farm[nx][ny] != "#":
                visit[nx][ny] = 1
                queue.append([nx, ny])
    if wo < sh:
        sheep += sh
    else:
        wolf += wo






for i in range(R):
    for j in range(C):
        if farm[i][j] != "#" and visit[i][j] == 0:
            bfs(i, j)


print(sheep, wolf)