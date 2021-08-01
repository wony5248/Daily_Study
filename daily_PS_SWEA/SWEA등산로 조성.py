from collections import deque
T = int(input())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    check = [[1 for _ in range(N)] for _ in range(N)]
    tmp = 0
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and mountain[nx][ny] < mountain[cx][cy]:
                check[nx][ny] = check[cx][cy] + 1
                if check[nx][ny] > tmp:
                    tmp = check[nx][ny]
                queue.append([nx, ny])
    final.append(tmp)

def down(count):
    if count == K+1:
        return
    for i in range(N):
        for j in range(N):
            mountain[i][j] = mountain[i][j] - count
            for k in range(N):
                for l in range(N):
                    if mountain[k][l] == maxV:
                        bfs(k, l)
            mountain[i][j] = mountain[i][j] + count
    down(count+1)


for tc in range(T):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    maxV =0
    final = []
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > maxV:
                maxV = mountain[i][j]
    down(1)


    print("#%d %d" %(tc+1, max(final)))