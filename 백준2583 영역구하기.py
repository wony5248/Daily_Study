M, N, K = map(int, input().split())
graph = [[0 for i in range(N)] for j in range(M)]


dx = [0,0,-1,1]
dy = [-1,1,0,0]
areanum = []
for i in range(K):
    lbx, lby, rux, ruy = map(int, input().split())
    for j in range(lby, ruy):
        for k in range(lbx, rux):
            graph[j][k] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = 1
            count =1
            queue = [[i,j]]
            while queue:
                x, y = queue[0][0], queue[0][1]
                del queue[0]
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<= nx <M and 0<= ny < N and graph[nx][ny] ==0:
                        graph[nx][ny] = 1
                        count += 1
                        queue.append([nx,ny])
            areanum.append(count)
print(len(areanum))
areanum.sort()
for i in areanum:
    print(i, end=" ")