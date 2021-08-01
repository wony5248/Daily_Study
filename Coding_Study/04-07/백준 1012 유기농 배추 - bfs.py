T = int(input())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for i in range(T):
    count = 0
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        y1, x1 = map(int, input().split())
        graph[x1][y1] = 1
    for j in range(N):
        for k in range(M):
            if graph[j][k] == 1 and visit[j][k] == 0:         # 배추이고 아직 방문하지 않았다면
                visit[j][k] = 1            
                count += 1                                    # 배추흰지렁이 한마리 추가
                queue = list()
                queue.append([j, k])
                while queue:                                  # 연결된 배추영역 다 방문
                    x, y = queue.pop(0)
                    for l in range(4):
                        nx = x + dx[l]
                        ny = y + dy[l]
                        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and visit[nx][ny] ==0:
                            visit[nx][ny] = 1
                            queue.append([nx, ny])
            else:
                continue
    print(count)



