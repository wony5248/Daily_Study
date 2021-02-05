M, N = map(int, input().split())
chess = [[0 for _ in range(N)] for _ in range(M)]
visit = [[0 for _ in range(N)] for _ in range(M)]
count = 0
dx = [0, -1, 0, 1, 1, -1, -1, 1]
dy = [-1, 0, 1, 0, -1, -1, 1, 1]
for i in range(M):
    vertex = list(map(int, input().split()))
    chess[i] = vertex
for i in range(M):
    for j in range(N):
        if chess[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            count += 1
            queue = list()
            queue.append([i, j])
            while queue:
                x, y = queue.pop(0)
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < M and 0 <= ny < N and chess[nx][ny] == 1 and visit[nx][ny] ==0:
                        visit[nx][ny] = 1
                        queue.append([nx, ny])
        else:
            continue
print(count)
