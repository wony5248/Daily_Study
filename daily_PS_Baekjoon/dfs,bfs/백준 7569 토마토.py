from collections import deque
M, N, H = map(int, input().split())
farm = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
visit = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
dx = [0, -1, 0, 1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()
count = 0

def bfs():
    global maxvalue
    maxvalue = 1
    while queue:
        cz, cx, cy = queue.popleft()
        visit[cz][cx][cy] = 1
        for d in range(6):
            nz = cz + dz[d]
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and farm[nz][nx][ny] == 0 and visit[nz][nx][ny] ==0:
                queue.append([nz, nx, ny])
                visit[nz][nx][ny] = 1
                farm[nz][nx][ny] = farm[cz][cx][cy] + 1
                if maxvalue < farm[nz][nx][ny]:
                    maxvalue = farm[nz][nx][ny]


for i in range(H):
    for j in range(N):
        farm[i][j] = list(map(int, input().split()))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if farm[i][j][k] == 1:
                queue.append([i,j,k])


bfs()


for i in range(H):
    for j in range(N):
        for k in range(M):
            if farm[i][j][k] == 0:
                count += 1

if count == 0:
    print(maxvalue - 1)
    # print(farm)
else:
    print(-1)


